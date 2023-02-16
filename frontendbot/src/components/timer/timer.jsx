
import { useEffect, useState } from "react"
import "./timer.css"


export default function Timer(){
    const [hour, setHour] = useState(0)
    const [minutes, setMinutes] = useState()
    

    var currentDate = new Date()
   
  
    
  
    useEffect(() =>{
            setHour(currentDate.getHours())
            setMinutes(currentDate.getMinutes())
    });
    function displayTime(){
        return "horas:"+hour+":horas:"+minutes
    }
    return(
        <>
            <div className="time" >
                <section className="display">
                     <span>
                        {23-hour}
                    </span>
                    <p>Horas</p>
                </section>
                <section className="display" >
                     <span>
                        {60-minutes}
                    </span>
                    <p>Minutos</p>
                </section>
                    
           </div>
        </>
    )
}