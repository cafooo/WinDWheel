const multiplierEl = document.querySelector(".multiplier");
const cashoutButton = document.querySelector(".cashout-button");
const canvas = document.getElementById("crashGraph");
const ctx = canvas.getContext("2d");

canvas.width = canvas.clientWidth;
canvas.height = canvas.clientHeight;

let multiplier = 1.00;
let crashPoint = (Math.random() * 3 + 2).toFixed(2);
let running = true;
let x = 0;
let y = canvas.height;

// Анимация множителя
function updateMultiplier() {
    if (multiplier >= crashPoint) {
        multiplierEl.textContent = "💥 CRASH!";
        multiplierEl.style.color = "#ff0000";
        multiplierEl.style.textShadow = "0 0 20px rgba(255, 0, 0, 0.8)";
        running = false;
        return;
    }

    multiplier += 0.01;
    multiplierEl.textContent = `x${multiplier.toFixed(2)}`;
    multiplierEl.style.transform = `scale(${1 + multiplier / 50})`;
    setTimeout(updateMultiplier, 200);
}

// Анимация графика
function drawGraph() {
    if (!running) return;
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    ctx.beginPath();
    ctx.moveTo(0, canvas.height);
    
    x += 5;
    y -= 2;

    ctx.lineTo(x, y);
    ctx.strokeStyle = "#00ff88";
    ctx.lineWidth = 3;
    ctx.stroke();

    if (x < canvas.width) {
        requestAnimationFrame(drawGraph);
    }
}

// Клик по кнопке Cash Out
cashoutButton.addEventListener("click", () => {
    if (!running) return;
    
    running = false;
    cashoutButton.textContent = `💰 Вывод: x${multiplier.toFixed(2)}`;
    cashoutButton.style.background = "#00ff88";
    cashoutButton.style.boxShadow = "0px 4px 10px rgba(0, 255, 136, 0.5)";
});

// Запуск игры
updateMultiplier();
drawGraph();
