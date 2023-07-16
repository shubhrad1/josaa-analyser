import React from "react";
import Head from "./header.module.css"
import logo from "./favicon.png" 

const Header=()=>{
    return(
        <div className={Head.ribbon}>
            <a href="/"><img className={Head.icon} src={logo} alt="logo"></img>
            <span className={Head.title}>JOSAA_Analyer</span>
            </a>
        </div>
    );
}
export default Header;