
import "./renderData.css"
import axios from "axios"
import { useEffect, useState } from "react";
export default function RenderData(){
    const [response, setResponse] = useState([])
    useEffect(() => {
        getStrategy();
    }, []);
    async function getStrategy(){
        try {
            const method = 'get';
            const url = 'https://api-webscrappingbot.vercel.app/strategy/1';
            const resp = await axios[method](url);
            setResponse(resp.data)
        } catch (error) {
            console.error(error);
        }
    }

    return(
    <>
            <div className="data">
                <section className="dataTitle">
                    <h4>Filtros Configurados</h4>
                </section>
                <div className="tableArea">
                    <table className="dataTable">
                        <thead className="tableTitle">
                            <tr >
                                <th>Mercado</th>
                                <th>Odd-Min</th>
                                <th>Odd-Max</th>
                            </tr>
                        </thead>
                        <tbody className="tableRows">
                        
                            <tr >
                                <td>{response.market}</td>
                                <td>{response.oddMin}</td>
                                <td>{response.oddMax}</td>
                            </tr>
                            
                        </tbody>
                    </table>
                </div>
            </div>
    </>)
}