const products = [
    { id: 1, name: 'Product 1', price: 100 },
    { id: 2, name: 'Product 2', price: 200 },
    { id: 3, name: 'Product 3', price: 200 },
    { id: 4, name: 'Product 4', price: 200 },
]

const productsContainer = document.getElementById('products_list');

products.forEach(product => {
    const productDiv = document.createElement('div');
    productDiv.classList.add('product'); // Добавьте класс для стилизации

    // Заполняем блок данными
    productDiv.innerHTML = `
        <img src="https://avatars.githubusercontent.com/u/51032358?v=4" class="logo">
        <h3 class="ProductName">${product.name}</h3>
        <p class="Price">Цена: ${product.price} руб.</p>
        <button class="AddToCart">В корзину</button>
    `;

    // Добавляем блок в контейнер
    productsContainer.appendChild(productDiv);
});
