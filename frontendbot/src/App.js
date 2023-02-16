
import './App.css';
import Home from './components/home/home';
import Menu from './components/menu/menu';
import Route from './components/route/route';
import { BrowserRouter } from 'react-router-dom';


function App() {
  return (
    <>
      <BrowserRouter>
          <Menu></Menu>
          <Route></Route>
    </BrowserRouter>
    </>  
  );
}
export default App;
