function ModeSelector({onModeChange, disabled}) {
    return (
        <div className="container">
            <div className="row">
                <div className="col-3">
                    <h3>模式</h3>
                </div>
                <div className="col-4">
                    <select className="form-select" aria-label="mode" onChange={onModeChange}
                            disabled={disabled}>
                        <option value="auto" defaultValue>自动模式</option>
                        <option value="voice">声控模式</option>
                        <option value="manual">手动模式</option>
                    </select>
                </div>
            </div>
        </div>
    )
}