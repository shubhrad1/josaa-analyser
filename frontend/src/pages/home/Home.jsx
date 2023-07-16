import React from "react";
import Home from "./Home.module.css"
// import Typewriter from './Typewriter';
import Typewriter from 'typewriter-effect';





const HomePage = () => {

    return(
    <div className={Home.wrapper}>

        <div className={Home.header}>JOSAA_ANALYSER</div>

        <Typewriter 
            onInit={(typewriter)=>{
                typewriter.typeString()
                
                .pauseFor(2500)
                .deleteAll()
                .start();
            }}
            options={{
                strings: ['Analyze JOSAA Seat Allotment Data for IITs with data since 2016!', 
                'Interactive Graphs for better visualization & understanding!',
                'Analyze with us to plan your future in IITs!'
                ],
                delay:45,
                deleteSpeed:45,
                autoStart:true,
                loop:true,
            }}
            className={Home.Typewrite}
            
        />
        <a href="/analysis"><div className={Home.getStarted}>Get Started!</div></a>
    </div>
    );
}
export default HomePage;