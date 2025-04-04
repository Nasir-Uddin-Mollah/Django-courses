const loadproducts = () => {
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then(data => displayproducts(data))
}
const displayproducts = (products) => {
    const parent = document.getElementById('products');
    products.forEach(product => {
        const div = document.createElement('div');
        div.classList.add('card');
        div.innerHTML = `
           <img src="${product.image}" class="card-img-top mx-auto" alt="...">
            <div class="card-body lh-sm">
                <h5 class="card-title">${product.title}</h5>
                <p class="card-text">${product.description.slice(0, 50)}</p>
                <p><strong>Price:</strong> $${product.price}</p>
                <p><strong>Category:</strong> ${product.category}</p>
                <a href="prdt_details.html?id=${product.id}" class="btn btn-primary">Details</a>
            </div>
        `;
        parent.appendChild(div);
    });
}


const loadcategory = () => {
    fetch('https://fakestoreapi.com/products/categories')
        .then(res => res.json())
        .then(data => displaycategory(data))
}
const displaycategory = (categories) => {
    const parent = document.getElementById('products-categories');
    categories.forEach(category => {
        const div = document.createElement('div');
        div.classList.add('category');
        div.innerHTML = `
            <button class="btn btn-success" id="${category}">${category}</button>
        `;
        parent.appendChild(div);
    });
}


const loadproductdetails = () => {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    fetch(`https://fakestoreapi.com/products/${id}`)
        .then(res => res.json())
        .then(data => displayproductdetails(data))
}
const displayproductdetails = (product) => {
    const parent = document.getElementById('product-details');
    const div = document.createElement('div');
    div.classList.add('product', 'mb-3');
    div.innerHTML = `
        <div class="product-image-container">
            <img src="${product.image}" class="product-image mx-auto" alt="...">
        </div>
        <div class="card-body product-card-body mx-auto lh-sm">
            <h5 class="card-title">${product.title}</h5>
            <p class="card-text product-card-text">${product.description}</p>
            <p><strong>Price:</strong> $${product.price}</p>
            <p><strong>Category:</strong> ${product.category}</p>
            <a href="" class="btn btn-primary">Add to cart</a>
        </div>
    `;
    parent.appendChild(div);
}


const handleregistration = (event) => {
    event.preventDefault();
    const username = document.getElementById('registration-username').value;
    const email = document.getElementById('registration-email').value;
    const password = document.getElementById('registration-password').value;
    const info = { username, email, password };

    fetch('https://fakestoreapi.com/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(info)
    })
        .then(res => res.json())
        .then(data => console.log(data))
}


const handlelogin = (event) => {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const info = { username, password };

    fetch('https://fakestoreapi.com/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(info)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            localStorage.setItem('token', data.token);
            const token = localStorage.getItem('token');
            console.log(token);
            alert('Login Successful!');
            window.location.href = 'index.html';
        })
}


const loadallusers = () => {
    fetch('https://fakestoreapi.com/users')
        .then(res => res.json())
        .then(data => {
            const parent = document.getElementById("table-body");
            data.forEach((user) => {
                const div = document.createElement('tr');
                div.innerHTML = `
                    <td>${user.id}</td>
                    <td>${user.name.firstname} ${user.name.lastname}</td>
                    <td>${user.email}</td>
                    <td>${user.phone}</td>
                    <td>${user.address.street}</td>
                    <td>${user.address.city}</td>
                    <td>${user.address.zipcode}</td>
                `;
                parent.appendChild(div);
            });
        })
}


loadproducts()
loadcategory()
loadproductdetails()
loadallusers()