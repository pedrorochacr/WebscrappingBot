

import axios from "axios"
import {  useRef, useState } from "react"
import "./saveData.css"
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
const defaultStrategy= {
    strategy: {
        market: '',
        oddMin: '',
        oddMax:''             
    }
    
}

export default function SaveData(){
    let formRef = useRef()
    const [strategy, setStrategy] = useState([])
    function handleInputChange(event) {
        const { name, value } = event.target;
        setStrategy({ ...strategy, [name]: value });
    }
    async function save(event){
        try {
            alert('Dados submetidos com sucesso!');
            const method = 'put';
            
            const url = 'https://api-webscrappingbot.vercel.app/strategy/1';
            const resp = await axios[method](url, strategy);
           
           formRef.current?.reset()
            console.log(resp);
        } catch (error) {
            console.error(error);
        }
    }
    return(
        <>
            <section className="formData">
                <h4 >Mercado</h4>
                <form ref={formRef}>
                    <select className="selectMarket" name="market" value={strategy.market} onChange={handleInputChange}>
                        <option selected disabled > Selecione uma opção</option>
                        <option value="Todos">Todos</option>
                        <option value="OverGols">OverGols</option>
                        <option value="UnderGols">UnderGols</option>
                        <option value="1x2">Vencedor</option>
                        <option value="AmbasMarcam">Ambas Marcam</option>
                        <option value="HA">Handicap Asiático</option>
                    </select>
                    <h4  >Odd Range</h4>
                    <div className="minMax">
                        <label>Min</label>
                        <input type="text" placeholder="00.00" name="oddMin" value={strategy.oddMin} onChange={handleInputChange} />
                        <label>Máx</label>
                        <input type="text" placeholder="15.00" name="oddMax" value={strategy.oddMax} onChange={handleInputChange} />
                    </div>
                
                </form>
                <button className="saveButton" onClick={e=>save(e)} >Salvar</button>
            </section>
            
        </>
    )
}