function ManualController({disabled, disableForm}) {
    const [baseAngle, setBaseAngle] = React.useState(0)
    const [gearAngle, setGearAngle] = React.useState(0)

    const requestShoot = (e) => {
        console.log('click button')
        sendRequest('POST', '/shoot')
        disableForm()
    }

    const requestAngleChange = (e) => {
        console.log(`request angle: ${baseAngle}, ${gearAngle}`);
        sendRequest('POST', `/angle/${baseAngle}/${gearAngle}`)
        disableForm()
    }

    const onBaseAngleChange = (e) => {
        if (e.target.value === null) {
            e.target.value = 0;
        } else if (e.target.value < 0) {
            e.target.value = 0
        } else if (e.target.value > 180) {
            e.target.value = 180
        }
        setBaseAngle(e.target.value)
    }

    const onGearAngleChange = (e) => {
        if (e.target.value === null) {
            e.target.value = 0;
        } else if (e.target.value < 0) {
            e.target.value = 0
        } else if (e.target.value > 180) {
            e.target.value = 180
        }
        setGearAngle(e.target.value)
    }

    return (
        <div className="container">
            <div className="row justify-content-start">
                <div className="col-2">
                    <input type="number" className="form-control"
                           aria-describedby="底座角度"
                           placeholder={'底座角度'}
                           onChange={onBaseAngleChange}
                           value={baseAngle}
                           min="0"
                           max="180"
                    />
                </div>
                <div className="col-2">
                    <input type="number" className="form-control"
                           aria-describedby="舵机角度"
                           placeholder={'舵机角度'}
                           onChange={onGearAngleChange}
                           value={gearAngle}
                           min="0"
                           max="180"
                    />
                </div>
                <button type="button" className="btn btn-primary col-1"
                        onClick={requestAngleChange}
                        disabled={disabled}>
                    旋转
                </button>
                <button type="button" className="btn btn-primary col-1" style={{marginLeft: '20px'}}
                        onClick={requestShoot}
                        disabled={disabled}>
                    发射
                </button>
            </div>
        </div>
    )
}