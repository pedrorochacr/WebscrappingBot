import { useState } from "react"
import SaveData from "../../data/saveData/saveData"
import {IoIosTimer} from "react-icons/io"
import "./home.css"
import Timer from "../timer/timer"

export default function Home(){
    return(
        <>
            <div id="home" className="homePage">
                <div className="hour">
                    <IoIosTimer size={85} ></IoIosTimer>
                    <h4>Os novos dados serão enviados em:</h4>
                    <Timer></Timer>
                </div>
                <div className="strategy">
                    <SaveData></SaveData>
                </div>

            </div>
        </>
    )
}