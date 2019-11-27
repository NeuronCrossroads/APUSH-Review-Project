import * as p5 from 'p5';

let s = (sk) => {    
    sk.setup = () =>{
        let cnv = P5.createCanvas(window.innerWidth,window.innerHeight);
        cnv.style("display","block");
        cnv.style("position","absolute");
        cnv.style("top","0px");
        cnv.style("left","0px");
        P5.background(0);
    }

    sk.draw = () =>{

    }

    sk.windowResized = () => {
        P5.resizeCanvas(window.innerWidth,window.innerHeight);
        P5.background(0);
    }
}

const P5 = new p5(s);
P5.year;