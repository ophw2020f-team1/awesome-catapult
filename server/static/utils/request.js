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