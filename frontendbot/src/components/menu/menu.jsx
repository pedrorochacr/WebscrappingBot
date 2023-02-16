import { Link } from "react-router-dom"
import "./menu.css"
import robotIcon  from "../../assets/robotIcon.png"
import {BiData} from "react-icons/bi"
import {BsJournalText,BsCodeSlash} from "react-icons/bs"
export default function Menu(){
    return(
        <>
            <div className="leftMenu"> 
            <section className="robotIcon">
                <img src={robotIcon} ></img>
            </section>
                <section className="linksArea">
                    <BsJournalText size={38}></BsJournalText>
                    <Link to="/">Estratégia</Link>
                </section>
                <section className="linksArea">
                    <BiData size={38}></BiData>
                    <Link to="/data">Dados Salvos</Link>
                </section>
            </div>
        </>
    )
}