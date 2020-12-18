function sendRequest(method, url) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function () { // 状态发生变化时，函数被回调
        if (request.readyState === 4) { // 成功完成
            // 判断响应结果:
            if (request.status === 200) {
                // 成功，通过responseText拿到响应的文本:
                console.log('send successfully')
            } else {
                console.log('send failed')
            }
        }
    }
    request.open(method, url)
    request.send()
}

const App = () => {

    const [mode, setMode] = React.useState('auto')
    const [angle, setAngle] = React.useState(0)
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
        sendRequest('POST', '/mode/' + mode)
        disableForm()
    }

    const requestShoot = (e) => {
        console.log('click button')
        sendRequest('POST', '/shoot')
        disableForm()
    }

    const requestAngleChange = (e) => {
        console.log(`request angle: ${angle}`);
        sendRequest('POST', '/angle/' + angle)
        disableForm()
    }

    const onAngleChange = (e) => {
        if (e.target.value === null) {
            e.target.value = 0;
        } else if (e.target.value < 0) {
            e.target.value = 0
        } else if (e.target.value > 180) {
            e.target.value = 180
        }
        setAngle(e.target.value)
    }

    return (
        <div className="container">
            <div className="row">
                <h1>投石机控制器</h1>
            </div>
            <br/>
            <br/>
            <div className="row">
                <div className="col-2">
                    <h3>模式选择：</h3>
                </div>
                <div className="col-4">
                    <select className="form-select" aria-label="Default select example" onChange={onModeChange}
                            disabled={disabled}>
                        <option value="auto" defaultValue>自动模式</option>
                        <option value="voice">声控模式</option>
                        <option value="manual">手动模式</option>
                    </select>
                </div>
            </div>
            {mode === 'manual' ?
                (
                    <div className="container">
                        <br/>
                        <div className="row">
                            <div className="col-3">
                                <input type="number" className="form-control"
                                       aria-describedby="angle"
                                       placeholder={'Angle'}
                                       onChange={onAngleChange}
                                       value={angle}
                                       min="0"
                                       max="180"
                                />
                            </div>
                            <button type="button" className="btn btn-primary col-1"
                                    onClick={requestAngleChange}
                                    disabled={disabled}>
                                旋转
                            </button>
                            <button type="button" className="btn btn-primary col-1 offset-md-1"
                                    onClick={requestShoot}
                                    disabled={disabled}>
                                发射
                            </button>
                        </div>
                    </div>
                ) : null
            }
        </div>
    )
}