import React, { useEffect, useState } from "react";
import StyleAnalysis from "./Analysis.module.css";
import {Chart as Chartjs} from 'chart.js/auto';
import { Line } from 'react-chartjs-2';

// const url='http://localhost:8000/api/analyser'
const Anaysis = () => 
{
    const [tableData,setTableData] = useState([]);
    const [formData,setFormData] = useState({
        inst: '',
        branch: '',
        quota: '',
        seat_type: '',
        gender: '',
        year: '',
        round: ''

    });
    const [chartData,setChartData] = useState(null);
    const [options,setOptions] = useState([])

    useEffect(()=>{
        fetch('/api/enum')
            .then(response=>response.json())
            .then(data => setOptions(data))
            .catch(error=>console.error(error))
    },[]);

    const checkBoxfunc = event =>
    {
        if (event.target.checked)
        {
            document.getElementById("chart").style.display="inline-block";
        }
        else
        {
            document.getElementById("chart").style.display="none";
        }
    }
    const checkBoxfunc2 = event =>
    {
        if (event.target.checked)
        {
            document.getElementById("table").style.display="inline-block";
        }
        else
        {
            document.getElementById("table").style.display="none";
        }
    }

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]:e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch(`/api/analyser?inst=${formData.inst}&branch=${formData.branch}&seat_type=${formData.seat_type}&gender=${formData.gender}&year=${formData.year}&round=${formData.round}`,{method:'GET'})
            
            .then(response => response.json())
            .then(data => {
                setTableData(data)
                const chartData = {
                    labels: data.data.map(data=>data.round),
                    datasets: [
                        {
                            label:'Closing Rank',
                            data:data.data.map(data=>data.closerank),
                            fill:true,
                            borderColor: 'rgba(75,192,192,1)',
                        },
                        {
                            label:'Opening Rank',
                            data:data.data.map(data=>data.openrank),
                            fill:true,
                            borderColor: 'rgba(5,100,50,1)',
                        },
                    ],
                };
                setChartData(chartData);
            })
            .catch(error => console.error('Error:',error));
    };


    const lineConfig = {
        responsive: true,

        elements:{
            line:{
                tension:0.3,
            },
        },
    };


    const [selectedOption, setSelectedOption] = useState('');
        const handleOptionClick = (event) => {
        const clickedOption = event.target.value;
        setSelectedOption(clickedOption);
        };

    return(
    <div className={StyleAnalysis.wrapper}>
        <label>Analyze By:</label>
        <select value={selectedOption} onChange={handleOptionClick}>
            <option value="" disabled selected>Select....</option>
            <option value="inst" selected={selectedOption === "inst"}>Institute</option>
            <option value="branch" selected={selectedOption === "branch"}>Branch</option>
            <option value="year" selected={selectedOption === "year"}>Year</option>
        </select>

        <form onSubmit={handleSubmit} >

            <select name="inst" value={formData.inst} onChange={handleChange} placeholder="inst">
            <option value="">ALL</option>
                {options && options.institutes && options.institutes.map(inst => (
                    <option>{inst}</option>
                ))}
            </select>

            <select name="branch" value={formData.branch} onChange={handleChange} placeholder="branch">
            <option value="">ALL</option>
                {options && options.branches && options.branches.map(brn => (
                    <option>{brn}</option>
                ))}
            </select>

            <select  name="seat_type" value={formData.seat_type} onChange={handleChange} placeholder="seat_type">
            <option value="">ALL</option>
                {options && options.seat && options.seat.map(st => (
                    <option>{st}</option>
                ))}
            </select>

            <select  name="gender" value={formData.gender} onChange={handleChange} placeholder="gender">
            <option value="">ALL</option>
                {options && options.gender && options.gender.map(gn => (
                    <option>{gn}</option>
                ))}
            </select>

            <select  name="year" value={formData.year} onChange={handleChange} placeholder="year">
            <option value="">ALL</option>
                {options && options.year && options.year.map(yr => (
                    <option>{yr}</option>
                ))}
            </select>

            <select  name="round" value={formData.round} onChange={handleChange} placeholder="round">
            <option value="">ALL</option>
                {options && options.round && options.round.map(rnd => (
                    <option>{rnd}</option>
                ))}
            </select>

            <input type="submit"></input>
        </form>

        <label><input type="checkbox" id="chk1" onChange={checkBoxfunc2}></input>&nbsp;Show OR-CR Table</label><br />
        <label><input type="checkbox" id="chk2" onChange={checkBoxfunc}></input>&nbsp;Show Graphical Analysis</label>
        
        <table id="table" >
            <thead>
                <tr>
                    <th>Institute</th>
                    <th>Branch</th>
                    <th>Quota</th>
                    <th>SeatType</th>
                    <th>Gender</th>
                    <th>OR</th>
                    <th>CR</th>
                    <th>Year</th>
                    <th>Round</th>
                </tr>
            </thead>
            <tbody>
                {tableData && tableData.data && tableData.data.map(row => (
                    <tr key={row.id}>
                        <td>{row.institute}</td>
                        <td>{row.program}</td>
                        <td>{row.quota}</td>
                        <td>{row.seatType}</td>
                        <td>{row.gender}</td>
                        <td>{row.openrank}</td>
                        <td>{row.closerank}</td>
                        <td>{row.year}</td>
                        <td>{row.round}</td>
                    </tr>
                    ))}
            </tbody>
        </table>
        <div id="chart" style={{ width: '90vw', height: '400px', marginBottom: '100px', display: 'none' }}>
            {chartData && <Line data={chartData} options={lineConfig}/>}

        </div>
        
    </div>
    );
}

export default Anaysis;