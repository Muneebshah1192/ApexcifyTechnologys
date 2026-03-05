from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Advanced Game State Memory
history = {
    'user': [],
    'ai': [],
    'results': [] # Tracks outcomes from the user's perspective
}
# Tracks N-Gram patterns (sequences of moves)
pattern_memory = {}

def get_human_like_ai_move():
    choices = ['rock', 'paper', 'scissors']
    
    # Not enough data yet? Play randomly to test the waters.
    if len(history['user']) < 2:
        return random.choice(choices), "Opening Move: True Random"

    last_user_move = history['user'][-1]
    last_ai_move = history['ai'][-1]
    last_result = history['results'][-1]

    # STRATEGY 1: N-Gram Pattern Recognition (The "I know your combo" strat)
    # Checks if the user is repeating a specific 2-move or 3-move sequence
    for n in [3, 2]:
        if len(history['user']) >= n:
            recent_sequence = tuple(history['user'][-n:])
            if recent_sequence in pattern_memory and sum(pattern_memory[recent_sequence].values()) > 0:
                predictions = pattern_memory[recent_sequence]
                predicted_move = max(predictions, key=predictions.get)
                return counter_move(predicted_move), f"Pattern Match: Intercepting {predicted_move} sequence"

    # STRATEGY 2: Human Psychology (Win-Stay, Lose-Shift)
    # Humans rarely play randomly. They react to the previous round.
    if last_result == 'lose':
        # If a human loses, they subconsciously switch to the move that would have just beaten the AI.
        # E.g., User played Rock, AI played Paper. User lost. User is likely to switch to Scissors.
        predicted_user_move = counter_move(last_ai_move)
        return counter_move(predicted_user_move), f"Psychology: Predicting revenge shift to {predicted_user_move}"
        
    elif last_result == 'win':
        # If a human wins, they feel confident and often repeat the winning move.
        return counter_move(last_user_move), f"Psychology: Punishing a confident repeat of {last_user_move}"

    # STRATEGY 3: Meta-Game Analysis (The "You know that I know" strat)
    # If it was a draw, humans often assume the AI will change its move, so the human plays the counter to the draw.
    if last_result == 'draw':
        predicted_user_move = counter_move(last_user_move)
        return counter_move(predicted_user_move), "Meta-Game: Breaking the draw cycle"

    # Fallback
    return random.choice(choices), "Evading detection with random choice"

def counter_move(move):
    counters = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    return counters.get(move, 'rock')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    user_move = data.get('move')
    
    if user_move not in ['rock', 'paper', 'scissors']:
        return jsonify({'error': 'Invalid command'}), 400

    ai_move, logic_used = get_human_like_ai_move()
    
    # Determine result from the User's perspective
    if user_move == ai_move:
        result = "draw"
    elif (user_move == 'rock' and ai_move == 'scissors') or \
         (user_move == 'paper' and ai_move == 'rock') or \
         (user_move == 'scissors' and ai_move == 'paper'):
        result = "win"
    else:
        result = "lose"

    # --- Update the Advanced Memory Bank ---
    # Record patterns for Strategy 1
    if len(history['user']) >= 2:
        last_two = tuple(history['user'][-2:])
        if last_two not in pattern_memory:
            pattern_memory[last_two] = {'rock': 0, 'paper': 0, 'scissors': 0}
        pattern_memory[last_two][user_move] += 1
        
    if len(history['user']) >= 3:
        last_three = tuple(history['user'][-3:])
        if last_three not in pattern_memory:
            pattern_memory[last_three] = {'rock': 0, 'paper': 0, 'scissors': 0}
        pattern_memory[last_three][user_move] += 1

    # Update state histories
    history['user'].append(user_move)
    history['ai'].append(ai_move)
    history['results'].append(result)

    return jsonify({
        'ai_move': ai_move,
        'result': result,
        'logic': logic_used
    })

if __name__ == '__main__':
    app.run(debug=True)