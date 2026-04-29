/* BLUEPRINT-JS-START */
// 🚀 Auto-generado para python: 4/29/2026, 12:52:32 PM

'use strict';

console.log('✅ 22 funciones y 1 clases detectadas');

// Funciones interactivas
function demo_resource_path() {
    console.log('▶️ Ejecutando: resource_path()');
    alert('Función resource_path() ejecutada');
}

function demo_emit() {
    console.log('▶️ Ejecutando: emit()');
    alert('Función emit() ejecutada');
}

function demo_add_particles() {
    console.log('▶️ Ejecutando: add_particles()');
    alert('Función add_particles() ejecutada');
}

function demo_delete_particles() {
    console.log('▶️ Ejecutando: delete_particles()');
    alert('Función delete_particles() ejecutada');
}

function demo_semitone_ratio() {
    console.log('▶️ Ejecutando: semitone_ratio()');
    alert('Función semitone_ratio() ejecutada');
}

function demo_speed_ratio() {
    console.log('▶️ Ejecutando: speed_ratio()');
    alert('Función speed_ratio() ejecutada');
}

function demo_fexp() {
    console.log('▶️ Ejecutando: fexp()');
    alert('Función fexp() ejecutada');
}

function demo_fman() {
    console.log('▶️ Ejecutando: fman()');
    alert('Función fman() ejecutada');
}

function demo_decimal_sign() {
    console.log('▶️ Ejecutando: decimal_sign()');
    alert('Función decimal_sign() ejecutada');
}

function demo_abbreviate() {
    console.log('▶️ Ejecutando: abbreviate()');
    alert('Función abbreviate() ejecutada');
}

function demo_resetupgrades() {
    console.log('▶️ Ejecutando: resetupgrades()');
    alert('Función resetupgrades() ejecutada');
}

function demo_constrain() {
    console.log('▶️ Ejecutando: constrain()');
    alert('Función constrain() ejecutada');
}

function demo_PlayMusic() {
    console.log('▶️ Ejecutando: PlayMusic()');
    alert('Función PlayMusic() ejecutada');
}

function demo_save_game() {
    console.log('▶️ Ejecutando: save_game()');
    alert('Función save_game() ejecutada');
}

function demo_load_game() {
    console.log('▶️ Ejecutando: load_game()');
    alert('Función load_game() ejecutada');
}

function demo_reset() {
    console.log('▶️ Ejecutando: reset()');
    alert('Función reset() ejecutada');
}

function demo_checkenemyded() {
    console.log('▶️ Ejecutando: checkenemyded()');
    alert('Función checkenemyded() ejecutada');
}

function demo_draw_text() {
    console.log('▶️ Ejecutando: draw_text()');
    alert('Función draw_text() ejecutada');
}

function demo_prestige() {
    console.log('▶️ Ejecutando: prestige()');
    alert('Función prestige() ejecutada');
}

function demo_calcmax() {
    console.log('▶️ Ejecutando: calcmax()');
    alert('Función calcmax() ejecutada');
}

function demo_calcmax0() {
    console.log('▶️ Ejecutando: calcmax0()');
    alert('Función calcmax0() ejecutada');
}

function demo_distance_to() {
    console.log('▶️ Ejecutando: distance_to()');
    alert('Función distance_to() ejecutada');
}

// Clases detectadas
console.log('📦 Clase: ParticlePrinciple');

// 🛒 Lógica de Tienda Automática con MockServer
function addToCart(product, price) {
    const item = { 
        product, 
        price, 
        date: new Date().toLocaleString() 
    };
    
    if (window.MockServer) {
        MockServer.save('orders', item);
        console.log('📦 Pedido guardado:', item);
        
        // Disparar evento para actualizar historial
        window.dispatchEvent(new CustomEvent('orderUpdated'));
    } else {
        alert('¡' + product + ' añadido al carrito!');
    }
    updateCartUI();
}

function updateCartUI() {
    const badge = document.getElementById('cart-badge');
    if (badge && window.MockServer) {
        badge.innerText = MockServer.get('orders').length;
    }
}

console.log('🛍️ Sistema de Tienda Pro con Persistencia listo.');

// 📜 Sistema de Historial de Pedidos Automático
window.StoreHistory = {
    init() {
        console.log('📜 Historial de Tienda Activado');
        this.render();
        
        // Escuchar actualizaciones de pedidos
        window.addEventListener('orderUpdated', () => this.render());
        
        // También refrescar periódicamente o si cambia localStorage
        window.addEventListener('storage', () => this.render());
    },
    
    render() {
        const historyList = document.getElementById('order-history-list');
        if (!historyList || !window.MockServer) return;
        
        const orders = MockServer.get('orders').reverse(); // Ver los más nuevos primero
        
        if (orders.length === 0) {
            historyList.innerHTML = '<p style="color: #666; font-style: italic;">No hay pedidos registrados aún.</p>';
            return;
        }
        
        let html = '<table class="history-table">';
        html += '<thead><tr><th>Fecha</th><th>Producto</th><th>Precio</th><th>Acción</th></tr></thead>';
        html += '<tbody>';
        
        orders.forEach(order => {
            html += '<tr>';
            html += '<td>' + order.date + '</td>';
            html += '<td style="font-weight: bold;">' + order.product + '</td>';
            html += '<td style="color: #10b981; font-weight: bold;">' + order.price + '</td>';
            html += '<td><button class="btn-delete-sm" onclick="MockServer.delete(\'orders\', \'' + order.id_uuid + '\'); window.dispatchEvent(new CustomEvent(\'orderUpdated\'));">🗑️</button></td>';
            html += '</tr>';
        });
        
        html += '</tbody></table>';
        historyList.innerHTML = html;
        console.log('✅ Historial renderizado:', orders.length, 'pedidos');
    }
};

document.addEventListener('DOMContentLoaded', () => StoreHistory.init());

// 🧬 Servidor Universal de Datos (Multi-Use)
window.MockServer = {
    save(collection, data) {
        const items = JSON.parse(localStorage.getItem(collection) || '[]');
        items.push({ ...data, id_uuid: Math.random().toString(36).substr(2, 9) });
        localStorage.setItem(collection, JSON.stringify(items));
        console.log('📁 Guardado en ['+collection+']:', data);
        if (window.AdminConsole) AdminConsole.refresh();
    },
    get(collection) {
        return JSON.parse(localStorage.getItem(collection) || '[]');
    },
    delete(collection, id) {
        const items = this.get(collection).filter(i => i.id_uuid !== id);
        localStorage.setItem(collection, JSON.stringify(items));
        if (window.AdminConsole) AdminConsole.refresh();
    },
    clear(collection) {
        localStorage.removeItem(collection);
        if (window.AdminConsole) AdminConsole.refresh();
    }
};

// 🛠️ Consola de Administración Visual
window.AdminConsole = {
    isOpen: false,
    init() {
        const btn = document.createElement('div');
        btn.id = 'admin-btn'; btn.innerHTML = '🛠️';
        btn.onclick = () => this.toggle();
        document.body.appendChild(btn);

        const panel = document.createElement('div');
        panel.id = 'admin-panel';
        panel.innerHTML = '<h3>🛠️ Admin Console</h3><div id="admin-content"></div><button onclick="AdminConsole.toggle()">Cerrar</button>';
        document.body.appendChild(panel);
        this.refresh();
    },
    toggle() { 
        this.isOpen = !this.isOpen;
        document.getElementById('admin-panel').style.display = this.isOpen ? 'block' : 'none';
    },
    refresh() {
        const content = document.getElementById('admin-content');
        if (!content) return;
        let html = '';
        const collections = ['orders', 'highscores', 'logs', 'users'];
        collections.forEach(c => {
            const data = MockServer.get(c);
            if (data.length > 0) {
                html += '<h4>'+c.toUpperCase()+' ('+data.length+')</h4><table>';
                data.slice(-5).forEach(i => {
                    html += '<tr><td>'+JSON.stringify(i).substr(0,40)+'...</td><td><button onclick="MockServer.delete(\''+c+'\', \''+i.id_uuid+'\')">🗑️</button></td></tr>';
                });
                html += '</table>';
            }
        });
        content.innerHTML = html || '<p>Esperando datos...</p>';
    }
};
document.addEventListener('DOMContentLoaded', () => AdminConsole.init());

/* BLUEPRINT-JS-END */