import './css/style.css'
import constants from './utils/constants'

const Avatar = () => {
    return (
      <div>
          <img src={constants.avatar} className='avatar' alt='avatar' weight='10px'/>
          <div>Pavel Ilin</div>
      </div>
    );
  }
  
  export default Avatar;
  