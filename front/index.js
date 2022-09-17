const app = Vue.createApp({
    data() {
        return {
            name: '',
            precio: 0,
            cantidad: 0
        }
    },
    methods: {
        async formSubmit() {
            const id = await this.addProduct()
            console.log(id)
            this.produceMessage(id)
            this.clearForm()
        },
        async addProduct() {
            const { data } = await axios.post('http://127.0.0.1:5000/insert', {
                name: this.name,
                cantidad: this.cantidad,
                precio: this.precio
            })
            const { response } = data;
            const { id } = response;
            return id;
        },
        async produceMessage(id) {
            const { data } = await axios.post('http://127.0.0.1:5000/produce', {
                id_sync: id,
                name: this.name,
                cantidad: this.cantidad,
                precio: this.precio
            })
            console.log(data)
        },
        clearForm() {
            this.name = ''
            this.precio = 0
            this.cantidad = 0
        }
    }
})

app.mount('#app')