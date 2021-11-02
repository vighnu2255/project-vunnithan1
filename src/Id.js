export function Id(porps) {
    return (
        <div>
            <div>{porps.artistId}</div>
            <button onClick={porps.onClick}>Delete</button>
        </div>
    )
}