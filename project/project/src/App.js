import { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import JogadorList from './componte/jogadorList';
function App() {
  const [jogadorList, setJogadorList] = useState([{}]);
  const [jogadorNome, setJogadorNome] = useState('');
  const [jogadorIdade, setJogadorIdade] = useState('');
  const [jogadorTime, setJogadorTime] = useState('');
  const [jogadorId,setJogadorId] =useState('');

  // Carrega lista de jogadores ao iniciar
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/jogadores')
      .then(res => {
        setJogadorList(res.data);
      })
      .catch(err => {
        console.log('Erro ao buscar jogadores:', err);
      });
  }, []);

  // Função para adicionar novo jogador
  const adicionarJogador = () => {
    const id = Date.now(); 

    axios.post(`http://127.0.0.1:8000/inserir_jogador/${id}`, {
      
      jogador_name: jogadorNome,
      jogador_idade: jogadorIdade,
      jogador_time: jogadorTime
    })
      .then(res => {
        setJogadorNome('');
        setJogadorIdade('');
        setJogadorTime('');
        return alert("Jogador cadastrado com sucess") 
        
        
        
      })
      .then(res => setJogadorList(res.data))
      .catch(err => console.log('Erro ao inserir jogador:', err));
  };

  return (
    <div className='container'>
      <div
        className='mt-3 justify-content-center align-items-center mx-auto'
        style={{ width: "60vw", backgroundColor: "#ffffff" }}
      >
        <h2 className='text-center text-white bg-success card mb-1'>
          Gerenciamento de jogadores
        </h2>
        <h6 className='text-center text-white bg-success card mb-2 pb-2'>
          Informações dos jogadores
        </h6>

        <div className='card text-center'>
          <h5 className='card text-center text-white bg-dark pb-1'>
            Cadastro Jogador
          </h5>

          <span className='card-text'>
            <input value={jogadorNome} onChange={(e) => setJogadorNome(e.target.value)} type='text' className='mb-2 form-control' placeholder='Informe o Nome:' />
            <input value={jogadorIdade} onChange={(e) => setJogadorIdade(e.target.value)} type='number' className='mb-2 form-control' placeholder='Informe a idade:' />
            <input value={jogadorTime} onChange={(e) => setJogadorTime(e.target.value)} type='text' className='mb-2 form-control' placeholder='Informe o Time:' />
          </span>

          <button className='btn btn-outline-success mb-4' onClick={adicionarJogador}>
            Cadastrar
          </button>

          <h5 className='text-center text-white bg-dark card mb-2'>
            Lista de jogadores
          </h5>
          <div>
            <JogadorList jogadorList={jogadorList}
            setJogadorId = {setJogadorId}
            setJogadorNome = {setJogadorNome}
            setJogadorIdade = {setJogadorIdade}
            setJogadorTime = {setJogadorTime}

            
            />

          </div>

          
        

          <h6 className='text-center text-white bg-success card mb-2'>
            &copy; CodeTI - 2025
          </h6>
        </div>
      </div>
    </div>
  );
}

export default App;
