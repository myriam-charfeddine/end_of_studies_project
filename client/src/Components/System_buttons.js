import r2wc from 'react-to-webcomponent';
import ReactDOM from 'react-dom';
import axios from 'axios'
import React, { useEffect, useState } from 'react'
import './System_buttons.css'
import LiveSysModal from './LiveSysModal';
import LangSwitcher from './LanguageSwitcher'
import LangSwitch from './LangSwitch';



const System_buttons = () => {

    let [rec, setRec] = useState(false)
    let [trans, setTrans] = useState("")
    let [pred, setPred] = useState("")
    let [feedback, setFeedback] = useState("")
    let [session_feedback, setSessionFeedback] = useState("")
    let [pipeline_feedback, setPipelineFeedback] = useState("")
    let [loadTrans, setLoadTrans] = useState(false)
    let [loadPred, setLoadPred] = useState(false)
  
    async function record(){
      setRec(true)
      setLoadPred(true)
      setLoadTrans(true)
      setTrans("")
      setPred("")
      setFeedback("")
      setSessionFeedback("")
      setPipelineFeedback("")
      await axios({
        method: "POST",
        url:'record_with_time_out'
      })
      .then(() => {
      setRec(false)
      setLoadTrans(false)
      setLoadPred(false)
      })
    }
  
    async function getTrans(){
      await axios({
        method: "GET",
        url:'get_transcription'
      })
      .then((response) => {
        setTrans(response.data)
      })
    }
  
    async function getPred(){
      await axios({
        method: "GET",
        url:'get_prediction'
      })
      .then((response) => {
        setPred(response.data)
      })
    }
  
    async function runScript(){
      await axios({
        method: "GET",
        url:'run_script'
      })
      .then((response) => {
      })
    }
  
    async function speechToScript() {
      await record();
      // setRec(false);
      await getTrans();
      await getPred();
      await get_pipeline_feedback()
      await get_session_feedback();
      await get_feedback();
  }
  
    async function startFirefoxSession(){
      await axios({
        method: "GET",
        url:'connect_to_pts_via_firefox'
      })
    }
  
    async function startChromeSession(){
      await axios({
        method: "GET",
        url:'connect_to_pts_via_chrome'
      })
    }
  
    async function get_session_feedback(){
      await axios({
        method: "GET",
        url:'get_session_feedback'
      })
      .then((response) => {
        setSessionFeedback(response.data)
      })
    }
  
    async function get_feedback(){
      await axios({
        method: "GET",
        url:'get_feedback'
      })
      .then((response) => {
        setFeedback(response.data)
      })
    }
  
    async function get_pipeline_feedback(){
      await axios({
        method: "GET",
        url:'get_pipeline_feedback'
      })
      .then((response) => {
        setPipelineFeedback(response.data)
      })
    }
  

  
    let [hover, setHover] = useState(false)


    // ...........
    useEffect(() => {
    async  function keyDownHandler(e) {
        if (e.key === "Enter") {
          // alert('The sky is your starting point!')
          await record();
          // setRec(false);
          await getTrans();
          await getPred();
          await get_pipeline_feedback()
          await get_session_feedback();
          await get_feedback();
        }
      }
      document.addEventListener("keydown", keyDownHandler);
    
    }, [])

 
  
  

  return (
    <div class="asr_buttons">
    <LangSwitch/>
    {/* <div class='asr_buttons'> */}
    <button class='btn' onClick={startFirefoxSession} onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}><img src='/firefox.png' alt='vocal session'/>{hover && <span class="button-text">Firefox vocal session</span>}</button>
    <button class='btn' onClick={startChromeSession} onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}><img src='/chrome.png' alt='vocal session'/>{hover && <span class="button-text">Chrome vocal session</span>}</button>
    <button  style={{
      backgroundColor: rec ? 'red' : 'white',
      transition: 'background-color 0.3s ease-in-out',
    }} class='btn' onClick={speechToScript}  onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}><img src='/micro.png' alt='mic'/>{hover && <span class="button-text">Voice command</span>}</button>
    <LiveSysModal trans={trans} pred={pred} feedback={feedback} session_feedback={session_feedback} pipeline_feedback={pipeline_feedback} loadPred={loadPred} loadTrans={loadTrans}/>

    {/* </div> */}
    
  </div>
  )
}

export default System_buttons

const SystemWebComp = r2wc(System_buttons, React, ReactDOM);
customElements.define('system-web-comp', SystemWebComp);