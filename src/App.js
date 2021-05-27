import Item from './Item'
import Avatar from './Avatar'
import './css/style.css'
import constants from './utils/constants'

const App = () => {
  const renderItems = () => {
    let id = 0
    return constants.items.map((result) => {
      id++
      return <Item key={id} result={result}/>
    })
  }

  return (
    <div>
      <div className="hello">
        <Avatar />
      </div>
      <div className="grid1">
        {renderItems()}
      </div>
      <div className="hello">
        <ul>
          <li><a href="https://www.linkedin.com/in/Pavel-Ilin">© Created by Pavel Ilin</a></li>
        </ul>
      </div>
    </div>
  );
}

export default App;
