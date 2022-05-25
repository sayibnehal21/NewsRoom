import React, { useState } from 'react'
import "../static/news.css"

function News() {
    const [news, setNews] = useState([{
        id:"",
        timestamp:"",
        subject:"",
        author:"",
        body:"",
        publisher:""
    }]);
    fetch("http://localhost:8080/get").then(response => {return response.json()}).then(data => {setNews(data)}).catch(error => console.log(error));

    return (
    <div>
        <ul>        
            {news.map(function(d, idx){
            return (<li key={idx}>
                    <h3>{d.timestamp}</h3>
                	<h1>{d.subject}</h1>
                    <p>{d.body}</p>
                    <h5>{d.author}</h5>
                    <button>Read more</button>
                    </li>)
            })}
        </ul>
    </div>
  )
}

export default News