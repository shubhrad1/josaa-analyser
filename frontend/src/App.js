import HomePage from "./pages/home/Home"
import Footer from "./parts/footer/footer";
import Header from "./parts/header/header"
import Analysis from "./pages/analysis/Analysis"
import ChartComponent from "./pages/analysis/Charts";
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Header />
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/analysis" element={<Analysis/>} />
          <Route path="/chart" element={<ChartComponent />} />
        </Routes>
      </Router>
      <Footer />
    </div>
  );
}

export default App;
