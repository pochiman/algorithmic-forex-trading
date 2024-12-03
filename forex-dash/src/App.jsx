import Test from "./Test";

function App() {

    const handleClick = (num) => {
        alert('handleClick:${num}');
    }    
    return (
        <div id="newdiv">
            Hello
                <Test surname="Smith" eyes="2" makeClick={handleClick} />
        </div>
    );
}

export default App;
