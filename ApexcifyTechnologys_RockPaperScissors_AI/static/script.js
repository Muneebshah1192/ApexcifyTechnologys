const emojis = { 'rock': '✊', 'paper': '✋', 'scissors': '✌️' };
let scores = { player: 0, ai: 0 };

async function play(playerChoice) {
    const buttons = document.querySelectorAll('.play-btn');
    const pHand = document.getElementById('player-hand');
    const aHand = document.getElementById('ai-hand');
    const arena = document.getElementById('arena');
    const statusText = document.getElementById('status-text');
    const logicText = document.getElementById('ai-logic');

    // 1. Reset interface and lock controls
    buttons.forEach(btn => btn.disabled = true);
    arena.className = 'arena'; // Strip result classes
    pHand.className = 'hand pump-left';
    aHand.className = 'hand ai-flip pump-right';
    
    pHand.textContent = '✊';
    aHand.textContent = '✊';
    statusText.textContent = "STRIKING";
    statusText.className = 'clash-indicator';
    logicText.textContent = "Processing behavioral sequence...";

    try {
        // 2. Fetch AI logic instantly in the background
        const response = await fetch('/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ move: playerChoice })
        });
        const data = await response.json();

        // 3. Wait exactly 1.2s for the CSS 'pump' animation to finish
        setTimeout(() => {
            // Reveal Moves
            pHand.textContent = emojis[playerChoice];
            aHand.textContent = emojis[data.ai_move];
            
            pHand.classList.remove('pump-left');
            aHand.classList.remove('pump-right');

            // Apply specific cinematic results
            if (data.result === 'win') {
                scores.player++;
                arena.classList.add('arena-win');
                statusText.textContent = "VICTORY";
                statusText.classList.add('text-win');
                pHand.classList.add('winner-float');
            } else if (data.result === 'lose') {
                scores.ai++;
                arena.classList.add('arena-lose');
                statusText.textContent = "DEFEAT";
                statusText.classList.add('text-lose');
                aHand.classList.add('winner-float');
            } else {
                arena.classList.add('arena-draw');
                statusText.textContent = "DRAW";
                statusText.classList.add('text-draw');
            }

            // Update DOM
            document.getElementById('player-score').textContent = scores.player;
            document.getElementById('ai-score').textContent = scores.ai;
            logicText.textContent = data.logic;

            // Unlock controls
            buttons.forEach(btn => btn.disabled = false);
        }, 1200);

    } catch (error) {
        console.error("Neural Link Failed", error);
        logicText.textContent = "ERR: Connection Lost";
        buttons.forEach(btn => btn.disabled = false);
    }
}