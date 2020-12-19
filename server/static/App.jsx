function App() {
    const [mode, setMode] = React.useState('auto')
    const [disabled, setDisabled] = React.useState(false)

    const disableForm = () => {
        setDisabled(true)
        setTimeout(() => {
            setDisabled(false)
        }, 1200)
    }

    const onModeChange = (e) => {
        console.log(`change mode to ${e.target.value}`)
        setMode(e.target.value)
        console.log(`set mode to ${mode}`)
        sendRequest('POST', '/mode/' + e.target.value)
        disableForm()
    }

    return (
        <div>
            <div className="container">
                <br/>
                <div className="row">
                    <h1>投石机控制器</h1>
                </div>
                <br/>
                <ModeSelector disabled={disabled} onModeChange={onModeChange}/>
                <br/>
                {mode === 'manual' ? <ManualController disabled={disabled} disableForm={disableForm}/> : null}
            </div>
        </div>
    )
}