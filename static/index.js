// for each connect button, add a click event listener to call /connect, passing device name in JSON body, and switch button visibility
document.querySelectorAll('.connect-btn').forEach((button) => {
    button.addEventListener('click', async (event) => {
        event.preventDefault()   
        const deviceName = button.closest('.device-remote').dataset.deviceName
        console.log(`Connect ${deviceName}`)

        const spinner = button.querySelector('.spinner')
        spinner.classList.remove('hidden')

        try {
            const payload = { device_name: deviceName }
            const response = await fetch('/connect', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            })

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`)
            }
            
            const data = await response.json()
            console.log(data)
        } catch (error) {
            console.log('Request failed:', error)
        }

        spinner.classList.add('hidden')

        button.classList.add('hidden')
        const disconnectButton = button.nextElementSibling
        disconnectButton.classList.remove('hidden')
    })
})

// for each remote button, add a click listener to call /perform, passing device name and remote action in JSON body
document.querySelectorAll('.remote-btn').forEach((button) => {
    button.addEventListener('click', async (event) => {
        event.preventDefault()
        const deviceName = button.closest('.device-remote').dataset.deviceName
        const remoteAction = button.dataset.remoteAction
        console.log(`Perform ${remoteAction} on ${deviceName}`)

        try {
            const payload = { device_name: deviceName, action: remoteAction }
            const response = await fetch('/perform', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload),
            })

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`)
            }

            const data = await response.json()
            console.log(data)
        } catch (error) {
            console.log('Request failed:', error)
        }
    })
})

// for each disconnect button, add a click event listener to call /disconnect, passing device name in JSON body, and switch button visibility
document.querySelectorAll('.disconnect-btn').forEach((button) => {
    button.addEventListener('click', async (event) => {
        event.preventDefault()
        const deviceName = button.closest('.device-remote').dataset.deviceName
        console.log(`Disconnect ${deviceName}`)

        const spinner = button.querySelector('.spinner')
        spinner.classList.remove('hidden')
        
        try {
            const payload = { device_name: deviceName }
            const response = await fetch('/disconnect', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            })

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`)
            }
            
            const data = await response.json()
            console.log(data)
        } catch (error) {
            console.log('Request failed:', error)
        }

        spinner.classList.add('hidden')

        button.classList.add('hidden')
        const connectButton = button.previousElementSibling
        connectButton.classList.remove('hidden')
    })
})