let canvas = document.getElementById('canv');
let ctx = canvas.getContext('2d');




class Cell{
    x = canvas.width = window.innerWidth;
    y = canvas.height = window.innerHeight;
    r = 3;
    direction = 0;
    speed = 1;

    update() {
        let dir = Math.PI * this.direction / 180;

        this.x += Math.cos(dir) * this.speed;
        this.y += Math.sin(dir) * this.speed;
    }

    draw( ctx ){
        ctx.beginPath();
        ctx.fillStyle = '#0d42a1';
        ctx.arc(this.x,this.y,this.r, 0, 2 * Math.PI);
        ctx.fill();
    }
    randomData() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.speed = 1 * Math.random() + 0.01;
        this.direction = Math.random() * 360;
    }
}




let cellList = [];

for(let i=0; i<100; i++){
    let cell = new Cell();
    cell.randomData();
    cellList.push(cell);

}

function drawCellLine(cellList){
    let copyCellList = cellList.slice();
    let limit = 160;
    while(copyCellList.length > 0) {
        let cell = copyCellList.pop();
        for (i=0; i<copyCellList.length; i++){
            let iCell = copyCellList[i];
            let rx = Math.pow(cell.x -iCell.x, 2);
            let ry = Math.pow(cell.y -iCell.y, 2);
            let distance = Math.sqrt(rx + ry);
            if(distance < limit) {
                ctx.beginPath();
                ctx.strokeStyle = '#0d42a1';
                ctx.lineWidth = 2 * (limit - distance) / limit;
                ctx.moveTo(cell.x, cell.y);
                ctx.lineTo(iCell.x, iCell.y);
                ctx.stroke();
            }
        }
    }
}

function update() {

    ctx.clearRect(0 , 0 , canvas.width, canvas.height);
    for(let i = 0; i < cellList.length; i++){
        let cell = cellList[i];
        cell.update();
        cell.draw( ctx );

        if(cell.x < 0 || cell.x > canvas.width || cell.y < 0 || cell.y > canvas.height){
        cell.randomData();
        }
    }

    drawCellLine(cellList);

}
setInterval(update, 10.0);
