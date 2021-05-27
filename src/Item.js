import './css/style.css'
const Item = (props) => {
    console.log(props.result.pic)

    return (
      <div className="g1">
        <a href={props.result.url}>{props.result.text}
          <img src={props.result.pic} className='avatar' alt='avatar'/>
        </a>
      </div>
    );
  }
  
  export default Item;
  