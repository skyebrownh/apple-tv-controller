const deviceRemotes = document.querySelectorAll('.device-remote')

// for each connect button, add a click event listener to call /connect, passing device name in JSON body, and switch button visibility
document.querySelectorAll('.connect-btn').forEach((button) => {
    button.addEventListener('click', async (event) => {
        event.preventDefault()   
        const deviceName = button.closest('.device-remote').dataset.deviceName
        console.log(deviceName)

        const spinner = button.querySelector('.spinner')
        spinner.classList.remove('hidden')
        await sleep(1000)
        spinner.classList.add('hidden')

        button.classList.add('hidden')
        const disconnectButton = button.nextElementSibling
        disconnectButton.classList.remove('hidden')
    })
})

// for each disconnect button, add a click event listener to call /disconnect, passing device name in JSON body, and switch button visibility
document.querySelectorAll('.disconnect-btn').forEach((button) => {
    button.addEventListener('click', async (event) => {
        event.preventDefault()
        const deviceName = button.closest('.device-remote').dataset.deviceName
        console.log(deviceName)

        const spinner = button.querySelector('.spinner')
        spinner.classList.remove('hidden')
        await sleep(1000)
        spinner.classList.add('hidden')

        button.classList.add('hidden')
        const connectButton = button.previousElementSibling
        connectButton.classList.remove('hidden')
    })
})



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}