import { Link } from "react-router-dom"
import "./menu.css"
import robotIcon from "../../assets/robotIcon.png"
import { BiData } from "react-icons/bi"
import { BsJournalText, BsCodeSlash } from "react-icons/bs"
import { useState } from "react"
import { FiAlignJustify } from 'react-icons/fi'



export default function Menu() {
    const [menuIconVisible, setMenuIconVisible] = useState(false)
    const [hamburguerClickedClass, sethamburguerClickedClass] = useState("hamburguerUnclicked")

    function renderizaLinksResponsivos(menuIconVisible) {
        if (menuIconVisible) {

            return <>
                <div className="linksMobile">
                    <section className="linksArea">
                        <BsJournalText size={38}></BsJournalText>
                        <Link onClick={updateMenu} to="/">Estratégia</Link>
                    </section>
                    <section className="linksArea">
                        <BiData size={38}></BiData>
                        <Link onClick={updateMenu} to="/data">Dados Salvos</Link>
                    </section>

                </div>
                
            </>
        }
    }
    const updateMenu = () => {
        if (menuIconVisible) {
            sethamburguerClickedClass("hamburguerUnclicked")
        }
        else {
            sethamburguerClickedClass("hamburguerButtonClicked")
        }
        setMenuIconVisible(!menuIconVisible)


    }
    return (
        <>
            <div className="leftMenu">
                <div className="desktopLinks">
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

            </div>
            <div className="responsiveMenu">
                <div className={hamburguerClickedClass}>
                    <button onClick={updateMenu} >
                        <FiAlignJustify size={45} ></FiAlignJustify>
                    </button>

                    {renderizaLinksResponsivos(menuIconVisible)}

                </div>
            </div>



        </>
    )
}