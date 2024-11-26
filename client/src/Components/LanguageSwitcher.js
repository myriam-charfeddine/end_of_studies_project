import axios from "axios";
import React, { Component, useEffect, useState } from "react";
import SwitchSelector from "react-switch-selector";

const options = [
    {
        label: <span>En</span>,
        value: {
             En: true
        },
        selectedBackgroundColor: "#FFBF00", //#0097e6
    },
    {
        label: "Tu",
        value: "Tu",
        selectedBackgroundColor: "#FFBF00"
    }
 ];
 

const LangSwitcher = () => {

let [lang, setLang] = useState("En")

async function change_language(){
        await axios({
          method: "POST",
          url:'change_language'
        })
        .then((response) => {
          console.log(response)
          setLang(response.data)
        })
      }

useEffect(() => {}, [lang]);

const onChange = (newValue) => {
        console.log(newValue);
       //  console.log(newValue=='Tu')
       change_language()
    };
    
const initialSelectedIndex = options.findIndex(({value}) => value === "En");

 return (
     <button className="your-required-wrapper" style={{width: 80, height: 30, border: 'none', background: 'none', color: 'black', }}>
         <SwitchSelector 
             onChange={onChange}
             options={options}
             initialSelectedIndex={initialSelectedIndex}
             backgroundColor={"#9da4b2"} //#353b48
             fontColor={"black"}  //#f5f6fa
         />
     </button>
    // <button onClick={change_language}>{lang}</button>
 );
}

export default LangSwitcher