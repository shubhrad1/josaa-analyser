import React from "react";
import Foot from "./footer.module.css" 

const Footer=()=>{
    return(
        <div className={Foot.ribbon}>
        <p className={Foot.copyright}>Copyright © 2023 Shubhradeep Das</p>
        <p className={Foot.developer}>Developed with <span class={Foot.heart}>&#x2764;</span> by shubhrad1<br></br>
        <div className={Foot.social}>
            <a href="https://www.facebook.com/profile.php?id=100055850841945"><i className="bi bi-facebook"></i></a>
            <a href="https://twitter.com/shubhrad1"><i className="bi bi-twitter"></i></a>
            <a href="https://github.com/shubhrad1"><i className="bi bi-github"></i></a>
            <a href="https://www.instagram.com/shubhrad.01/"><i className="bi bi-instagram"></i></a>
            <a href="https://www.linkedin.com/in/shubhradeepdas/"><i className="bi bi-linkedin"></i></a>
        </div>
        </p>
        </div>
    );
}
export default Footer;
