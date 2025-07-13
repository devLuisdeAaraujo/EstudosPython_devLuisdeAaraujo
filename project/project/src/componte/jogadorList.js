import React from "react";
import Jogador from "./jogador";

function JogadorList(props){
    return (
        <div>
            <ul>
                {
                    props.jogadorList.map(
                        (jogador,indice) => {
                            return(<Jogador jogador={jogador} key={indice}></Jogador>)
                        })
                    }
            </ul>
        </div>
    )

}
export default JogadorList