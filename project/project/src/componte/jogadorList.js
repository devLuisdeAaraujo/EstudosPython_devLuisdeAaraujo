import React from "react";
import Jogador from "./jogador";

function JogadorList(props){
    return (
        <div>
            <ul>
                {
                    props.jogadorList.map(
                        (jogador,indice) => {
                            return(<Jogador 
                                jogador={jogador} 
                                key={indice}
                                setJogadorId={props.setJogadorId}
                                setJogadorNome={props.setJogadorNome}
                                setJogadorIdade = {props.setJogadorIdade}
                                setJogadorTime  = {props.setJogadorTime}>
                                </Jogador>)
                        })
                    }
            </ul>
        </div>
    )

}
export default JogadorList