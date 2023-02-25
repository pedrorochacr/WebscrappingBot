
import "./renderData.css"
import axios from "axios"
import { useEffect, useState } from "react";
import { firebaseApp } from "../firebaseconfig/firebaseInit";
import {
    getFirestore,
    collection,
    addDoc,
    doc,
    deleteDoc,
    getDocs,
} from "firebase/firestore";
export default function RenderData() {

    const db = getFirestore(firebaseApp)
    const strategyCollection = collection(db, "strategy")
    const [response, setResponse] = useState([])
    useEffect(() => {
        let mounted = true
        const getStrategy = async () => {
            try {
                const data = await getDocs(strategyCollection)
                if (mounted) {
                    setResponse(data.docs.map((doc) => ({ ...doc.data(), id: doc.id })))
                }
            } catch (error) {
                console.error(error);
            }
        }
        getStrategy()
        return () => {
            mounted = false
        }
    }, [strategyCollection])

    return (
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

                            {response.map((item) => (
                                <tr key={item.id}>
                                    <td>{item.market}</td>
                                    <td>{item.oddMin}</td>
                                    <td>{item.oddMax}</td>
                                </tr>
                            ))}

                        </tbody>
                    </table>
                </div>
            </div>
        </>)
}