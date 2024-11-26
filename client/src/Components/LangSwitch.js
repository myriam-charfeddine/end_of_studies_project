import React, { useEffect, useState } from 'react'
import './LangSwitch.css'
import axios from 'axios'

const LangSwitch = () => {
    let [lang, setLang] = useState("En")

    async function change_language(){
            await axios({
              method: "POST",
              url:'change_language'
            })
            .then((response) => {
            // //   console.log(response)
              setLang(response.data)
            })
          }
    
    useEffect(() => {}, [lang]);

  return (
    <div class="container">
	<div class="input-switch">
		<label for="switchy">En</label>
		<input type="checkbox" id="switchy" class="input" />
		<label for="switchy" class="switch" onClick={change_language}></label>
		<label for="switchy">Tu</label>
	</div>
</div>



  )
}

export default LangSwitch