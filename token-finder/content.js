// Kiểm tra nếu nút đã được thêm để tránh thêm nhiều lần
if (!document.getElementById('my-extension-button')) {
    // Tạo nút mới
    const button = document.createElement('button');
    button.id = 'my-extension-button';
    button.innerText = 'Click Me!';
    button.style.position = 'fixed';
    button.style.bottom = '20px';
    button.style.right = '20px';
    button.style.zIndex = '10000';
    button.style.padding = '10px 15px';
    button.style.backgroundColor = '#0078D7';
    button.style.color = '#fff';
    button.style.border = 'none';
    button.style.borderRadius = '5px';
    button.style.cursor = 'pointer';
    button.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
  
    // Thêm sự kiện click cho nút
    button.addEventListener('click', () => {
      alert('Bạn vừa nhấn nút!');
      displayLocalStorageKeys();
      fillLoginForm();
      displayLocalStorageValue('XAX');
    });
  
    // Thêm nút vào body của trang
    document.body.appendChild(button);
}

// Hàm hiển thị danh sách các keys của localStorage
function displayLocalStorageKeys() {
    const keys = Object.keys(localStorage);
    console.log('LocalStorage Keys:', keys);
}

// Hàm điền giá trị vào form đăng nhập
function fillLoginForm() {
    const loginIdInput = document.querySelector('input[name="LoginID"]');
    const passwordInput = document.querySelector('input[name="password"]');
    
    if (loginIdInput && passwordInput) {
        loginIdInput.value = 'yourLoginID'; // Thay 'yourLoginID' bằng giá trị thực tế
        passwordInput.value = 'yourPassword'; // Thay 'yourPassword' bằng giá trị thực tế
    } else {
        console.log('Không tìm thấy input với name="LoginID" hoặc name="password"');
    }
}

// Hàm hiển thị giá trị của key trong localStorage
function displayLocalStorageValue(key) {
    const value = localStorage.getItem(key);
    if (value) {
        try {
            const jsonValue = JSON.parse(value);
            const accessKey = jsonValue.AccessKey;
            if (accessKey) {
                prompt(`AccessKey for key "${key}":`, accessKey);
            } else {
                console.log(`Không tìm thấy AccessKey trong giá trị của key "${key}"`);
            }
        } catch (e) {
            console.log(`Giá trị của key "${key}" không phải là JSON hợp lệ`);
        }
    } else {
        console.log(`Không tìm thấy key "${key}" trong localStorage`);
    }
}