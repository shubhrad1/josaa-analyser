import React from "react";
import Home from "./Home.module.css"

const HomePage = () => {
    return(
    <div className={Home.wrapper}>
        <div className={Home.header}>JOSAA_ANALYSER</div>
        <div className={Home.descr}>Analyze JOSAA Seat Allotment Data for IITs for as early as 7 years! </div>
        
    </div>
    );
}
export default HomePage;