import React from "react";
import axios from "axios";

function Jogador(props){
    const excluiJogador = (id_jogador) =>{
        axios.delete(`http://127.0.0.1:8000/jogadores/${id_jogador}/limpar_campos/`)
            .then(
                respota =>{
                    alert("Jogador removido com sucesso"+respota.data)
                }
            )
    } 
    return (
        <div>
            <p>
                <span className = 'fw-bold'>
                    {props.jogador.nome} -{props.jogador.idade}-{props.jogador.time}
                </span>
                <button onClick={()=> excluiJogador(props.jogador.id)} className="btn sn">
                    <span className="badge rounded-pill bg-danger">
                        X
                    </span>

                </button>

            </p>
        </div>
    )
}

export default Jogador;