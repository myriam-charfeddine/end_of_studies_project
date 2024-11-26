import React, { useState } from 'react'
import './LiveSysModal.css'

const LiveSysModal = ({trans, pred, feedback, session_feedback, pipeline_feedback, loadPred, loadTrans}) => {
  let [hover, setHover] = useState(false)
  

  return (
    <span class="live_modal">
        <button class='btn' onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}><a href="#modal-opened" class="link-1" id="modal-closed"><img src='/live.png' alt='live'/></a>{hover && <span class="button-text">Check live output</span>}</button>

    <div class="modal-container" id="modal-opened">
      <div class="modal">
    
        <div class="modal__details">
          <h1 class="modal__title">Live output</h1>
          {!loadTrans ? <p class="modal__description">{trans}</p> : <div class="loader"></div> }
          {!loadPred ? <p class="modal__description">{pred}</p> : <div class="loader"></div> }
          { (pred!=='None' ) ? (feedback ? <p class="modal__description_feedback">{feedback}</p> : "")  : ""}
          { (pred!=='None' ) ? (session_feedback ? <p class="modal__description_feedback">{session_feedback}</p> : "")  : ""}
          { (pred ) ? (pipeline_feedback ? <p class="modal__description_feedback">{pipeline_feedback}</p> : "")  : ""}
        </div>
    
        <a href="#modal-closed" class="link-2"></a>
    
      </div>
    </div>
    
  </span>
  )
}

export default LiveSysModal