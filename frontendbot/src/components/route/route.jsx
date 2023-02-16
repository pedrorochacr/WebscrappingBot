import React from "react";
import {Routes, Route} from 'react-router-dom'
import RenderData from "../../data/renderData/renderData";
import Home from "../home/home";




export default props =>
    <Routes>
        <Route exact path='/' element={<Home></Home>}/>
        <Route exact path='/data' element={<RenderData></RenderData>}></Route>
        <Route path='*' element={<Home />}/>
    </Routes>