import React, { useState, useEffect } from 'react';
import { ShoppingBag, Bike, User, Settings, Home, LogOut, Plus, Trash2, MapPin } from 'lucide-react';

export default function UbiApp() {
  const [user, setUser] = useState(null);
  const [page, setPage] = useState('home');
  const [restaurants, setRestaurants] = useState([
    {
      id: 1,
      name: 'مطعم الأمير',
      type: 'مطعم',
      image: 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=400',
      phone: '0555123456',
      location: 'ورقلة، الرويسات',
      meals: [
        { id: 1, name: 'كسكس باللحم', price: 450, image: 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=300' },
        { id: 2, name: 'شخشوخة', price: 350, image: 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=300' }
      ]
    },
    {
      id: 2,
      name: 'مطعم الواحات',
      type: 'مطعم',
      image: 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400',
      phone: '0556789012',
      location: 'ورقلة، حي الزيانية',
      meals: [
        { id: 3, name: 'طاجين لحم', price: 500, image: 'https://images.unsplash.com/photo-1544025162-d76694265947?w=300' },
        { id: 4, name: 'مثور', price: 400, image: 'https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=300' }
      ]
    }
  ]);
  const [cart, setCart] = useState([]);
  const [orders, setOrders] = useState([]);
  const [drivers, setDrivers] = useState([]);

  useEffect(() => {
    const savedUser = localStorage.getItem('ubiUser');
    if (savedUser) {
      try {
        setUser(JSON.parse(savedUser));
      } catch (e) {
        localStorage.removeItem('ubiUser');
      }
    }
  }, []);

  // صفحة تسجيل الدخول
  if (!user) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-100 to-white flex items-center justify-center p-4">
        <div className="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md">
          <div className="text-center mb-8">
            <div className="inline-block bg-gradient-to-br from-purple-600 to-purple-800 text-white p-6 rounded-full mb-4 shadow-lg">
              <span className="text-5xl font-bold">U</span>
            </div>
            <h1 className="text-4xl font-bold text-purple-600">Ubi</h1>
            <p className="text-gray-600 mt-2">خدمة التوصيل السريع - ورقلة</p>
          </div>

          <div className="space-y-4">
            <input
              type="email"
              id="email"
              placeholder="البريد الإلكتروني"
              className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
            />
            <input
              type="password"
              id="password"
              placeholder="كلمة المرور"
              className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
            />
            
            <label className="flex items-center cursor-pointer">
              <input
                type="checkbox"
                id="remember"
                defaultChecked
                className="ml-2 w-4 h-4"
              />
              <span className="text-gray-700">حفظ كلمة المرور</span>
            </label>

            <button
              onClick={() => {
                const email = document.getElementById('email').value;
                const password = document.getElementById('password').value;
                const remember = document.getElementById('remember').checked;
                
                if (email && password) {
                  const userData = {
                    email: email,
                    name: email.split('@')[0],
                    isAdmin: email === 'admin@ubi.com'
                  };
                  
                  setUser(userData);
                  
                  if (remember) {
                    localStorage.setItem('ubiUser', JSON.stringify(userData));
                  }
                }
              }}
              className="w-full bg-gradient-to-r from-purple-600 to-purple-800 text-white p-3 rounded-lg font-bold hover:from-purple-700 hover:to-purple-900 transition shadow-md"
            >
              تسجيل الدخول
            </button>
          </div>
        </div>
      </div>
    );
  }

  // الواجهة الرئيسية بعد تسجيل الدخول
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 to-white">
      {/* الهيدر */}
      <div className="bg-white shadow-md sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-br from-purple-600 to-purple-800 text-white p-3 rounded-full shadow-lg">
              <span className="text-2xl font-bold">U</span>
            </div>
            <div>
              <h1 className="text-2xl font-bold text-purple-600">Ubi</h1>
              <p className="text-xs text-gray-600">ورقلة</p>
            </div>
          </div>
          <div className="flex items-center gap-4">
            <span className="text-gray-700 hidden md:block">مرحباً، {user.name}</span>
            <button
              onClick={() => {
                setUser(null);
                localStorage.removeItem('ubiUser');
              }}
              className="text-red-600 hover:bg-red-50 p-2 rounded transition"
            >
              <LogOut size={20} />
            </button>
          </div>
        </div>
      </div>

      {/* القائمة */}
      <div className="bg-purple-600 text-white">
        <div className="container mx-auto px-4">
          <div className="flex gap-2 overflow-x-auto">
            <button
              onClick={() => setPage('home')}
              className={`px-6 py-3 flex items-center gap-2 transition whitespace-nowrap ${page === 'home' ? 'bg-purple-700' : 'hover:bg-purple-700'}`}
            >
              <Home size={20} />
              الرئيسية
            </button>
            <button
              onClick={() => setPage('cart')}
              className={`px-6 py-3 flex items-center gap-2 transition relative whitespace-nowrap ${page === 'cart' ? 'bg-purple-700' : 'hover:bg-purple-700'}`}
            >
              <ShoppingBag size={20} />
              السلة
              {cart.length > 0 && (
                <span className="absolute -top-1 -left-1 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-xs">
                  {cart.length}
                </span>
              )}
            </button>
            <button
              onClick={() => setPage('orders')}
              className={`px-6 py-3 flex items-center gap-2 transition whitespace-nowrap ${page === 'orders' ? 'bg-purple-700' : 'hover:bg-purple-700'}`}
            >
              <User size={20} />
              طلباتي
            </button>
            <button
              onClick={() => setPage('driver')}
              className={`px-6 py-3 flex items-center gap-2 transition whitespace-nowrap ${page === 'driver' ? 'bg-purple-700' : 'hover:bg-purple-700'}`}
            >
              <Bike size={20} />
              كن سائق
            </button>
            {user.isAdmin && (
              <button
                onClick={() => setPage('admin')}
                className={`px-6 py-3 flex items-center gap-2 transition whitespace-nowrap ${page === 'admin' ? 'bg-purple-700' : 'hover:bg-purple-700'}`}
              >
                <Settings size={20} />
                الإدارة
              </button>
            )}
          </div>
        </div>
      </div>

      {/* المحتوى */}
      <div className="container mx-auto px-4 py-8">
        {/* الصفحة الرئيسية */}
        {page === 'home' && (
          <div>
            <h2 className="text-3xl font-bold text-purple-600 mb-6">المطاعم والمحلات في ورقلة</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {restaurants.map(restaurant => (
                <div key={restaurant.id} className="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-2xl transition">
                  <img src={restaurant.image} alt={restaurant.name} className="w-full h-48 object-cover" />
                  <div className="p-6">
                    <div className="flex items-center justify-between mb-2">
                      <h3 className="text-xl font-bold">{restaurant.name}</h3>
                      <span className="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm font-semibold">
                        {restaurant.type}
                      </span>
                    </div>
                    <p className="text-gray-600 mb-1 flex items-center gap-2">
                      <MapPin size={16} /> {restaurant.location}
                    </p>
                    <p className="text-gray-600 mb-4">📞 {restaurant.phone}</p>
                    <div className="space-y-3">
                      {restaurant.meals.map(meal => (
                        <div key={meal.id} className="flex items-center justify-between border-t pt-3">
                          <div className="flex items-center gap-3">
                            {meal.image && <img src={meal.image} alt={meal.name} className="w-12 h-12 rounded object-cover" />}
                            <div>
                              <p className="font-semibold">{meal.name}</p>
                              <p className="text-purple-600 font-bold">{meal.price} دج</p>
                            </div>
                          </div>
                          <button
                            onClick={() => {
                              setCart([...cart, { restaurant: restaurant.name, meal: meal.name, price: meal.price }]);
                              alert('تم إضافة المنتج للسلة ✓');
                            }}
                            className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition"
                          >
                            <Plus size={20} />
                          </button>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* صفحة السلة */}
        {page === 'cart' && (
          <div className="max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-purple-600 mb-8">سلة المشتريات</h2>
            {cart.length === 0 ? (
              <div className="bg-white rounded-xl shadow-lg p-8 text-center">
                <ShoppingBag className="mx-auto mb-4 text-gray-400" size={64} />
                <p className="text-gray-600 text-lg mb-4">سلتك فارغة</p>
                <button
                  onClick={() => setPage('home')}
                  className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700 transition"
                >
                  تصفح المطاعم
                </button>
              </div>
            ) : (
              <div className="bg-white rounded-xl shadow-lg p-6">
                <div className="space-y-4 mb-6">
                  {cart.map((item, index) => (
                    <div key={index} className="flex justify-between items-center border-b pb-4">
                      <div>
                        <p className="font-bold">{item.meal}</p>
                        <p className="text-gray-600 text-sm">{item.restaurant}</p>
                      </div>
                      <div className="flex items-center gap-4">
                        <p className="text-purple-600 font-bold">{item.price} دج</p>
                        <button
                          onClick={() => setCart(cart.filter((_, i) => i !== index))}
                          className="text-red-600 hover:bg-red-50 p-2 rounded"
                        >
                          <Trash2 size={20} />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
                <div className="border-t pt-4">
                  <div className="flex justify-between items-center mb-6">
                    <span className="text-xl font-bold">المجموع:</span>
                    <span className="text-2xl font-bold text-purple-600">
                      {cart.reduce((sum, item) => sum + item.price, 0)} دج
                    </span>
                  </div>
                  <button
                    onClick={() => {
                      const total = cart.reduce((sum, item) => sum + item.price, 0);
                      setOrders([...orders, {
                        id: Date.now(),
                        items: [...cart],
                        total: total,
                        status: 'pending',
                        date: new Date().toLocaleString('ar-DZ')
                      }]);
                      setCart([]);
                      alert('تم تقديم طلبك بنجاح! ✓');
                      setPage('orders');
                    }}
                    className="w-full bg-gradient-to-r from-purple-600 to-purple-800 text-white p-4 rounded-lg font-bold hover:from-purple-700 hover:to-purple-900 transition shadow-md"
                  >
                    تأكيد الطلب
                  </button>
                </div>
              </div>
            )}
          </div>
        )}

        {/* صفحة الطلبات */}
        {page === 'orders' && (
          <div className="max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-purple-600 mb-8">طلباتي</h2>
            {orders.length === 0 ? (
              <div className="bg-white rounded-xl shadow-lg p-8 text-center">
                <p className="text-gray-600 text-lg mb-4">لا توجد طلبات</p>
                <button
                  onClick={() => setPage('home')}
                  className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700 transition"
                >
                  ابدأ الطلب الآن
                </button>
              </div>
            ) : (
              <div className="space-y-4">
                {orders.map(order => (
                  <div key={order.id} className="bg-white rounded-xl shadow-lg p-6">
                    <div className="flex justify-between items-start mb-4">
                      <div>
                        <p className="font-bold text-lg">طلب #{order.id}</p>
                        <p className="text-gray-600 text-sm">{order.date}</p>
                      </div>
                      <span className="px-4 py-2 rounded-full text-white font-semibold bg-yellow-500">
                        قيد التحضير
                      </span>
                    </div>
                    <div className="space-y-2 mb-4">
                      {order.items.map((item, index) => (
                        <div key={index} className="flex justify-between">
                          <span>{item.meal}</span>
                          <span className="text-purple-600">{item.price} دج</span>
                        </div>
                      ))}
                    </div>
                    <div className="border-t pt-4">
                      <div className="flex justify-between font-bold text-lg">
                        <span>المجموع:</span>
                        <span className="text-purple-600">{order.total} دج</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {/* صفحة التسجيل كسائق */}
        {page === 'driver' && (
          <div className="max-w-2xl mx-auto bg-white rounded-xl shadow-lg p-8">
            <h2 className="text-3xl font-bold text-purple-600 mb-6 text-center">التسجيل كسائق توصيل</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-gray-700 mb-2 font-semibold">الاسم الكامل</label>
                <input
                  type="text"
                  id="driverName"
                  className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
                />
              </div>
              <div>
                <label className="block text-gray-700 mb-2 font-semibold">رقم الهاتف</label>
                <input
                  type="tel"
                  id="driverPhone"
                  className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
                />
              </div>
              <div>
                <label className="block text-gray-700 mb-2 font-semibold">رقم بطاقة الهوية</label>
                <input
                  type="text"
                  id="driverId"
                  className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
                />
              </div>
              <div>
                <label className="block text-gray-700 mb-2 font-semibold">نوع المركبة</label>
                <select
                  id="vehicleType"
                  className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
                >
                  <option>سيارة</option>
                  <option>دراجة نارية</option>
                </select>
              </div>
              <div>
                <label className="block text-gray-700 mb-2 font-semibold">اسم المركبة</label>
                <input
                  type="text"
                  id="vehicleName"
                  placeholder="مثال: رينو كليو"
                  className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
                />
              </div>
              <div>
                <label className="block text-gray-700 mb-2 font-semibold">رقم اللوحة</label>
                <input
                  type="text"
                  id="vehiclePlate"
                  className="w-full p-3 border-2 border-purple-200 rounded-lg focus:border-purple-600 outline-none"
                />
              </div>
              <button
                onClick={() => {
                  const name = document.getElementById('driverName').value;
                  const phone = document.getElementById('driverPhone').value;
                  const idNum = document.getElementById('driverId').value;
                  const vType = document.getElementById('vehicleType').value;
                  const vName = document.getElementById('vehicleName').value;
                  const vPlate = document.getElementById('vehiclePlate').value;
                  
                  if (name && phone && idNum && vName && vPlate) {
                    setDrivers([...drivers, {
                      id: Date.now(),
                      name, phone, idNumber: idNum,
                      vehicleType: vType, vehicleName: vName, vehiclePlate: vPlate,
                      status: 'pending'
                    }]);
                    alert('تم إرسال طلب التسجيل بنجاح! ✓');
                    document.getElementById('driverName').value = '';
                    document.getElementById('driverPhone').value = '';
                    document.getElementById('driverId').value = '';
                    document.getElementById('vehicleName').value = '';
                    document.getElementById('vehiclePlate').value = '';
                  } else {
                    alert('الرجاء ملء جميع الحقول');
                  }
                }}
                className="w-full bg-gradient-to-r from-purple-600 to-purple-800 text-white p-3 rounded-lg font-bold hover:from-purple-700 hover:to-purple-900 transition shadow-md"
              >
                إرسال الطلب
              </button>
            </div>
          </div>
        )}

        {/* لوحة الإدارة */}
        {page === 'admin' && user.isAdmin && (
          <div className="max-w-6xl mx-auto">
            <h2 className="text-3xl font-bold text-purple-600 mb-8">لوحة التحكم</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h3 className="text-xl font-bold mb-4 text-purple-600">إحصائيات</h3>
                <div className="space-y-3">
                  <p className="text-gray-700">عدد المطاعم: <span className="font-bold">{restaurants.length}</span></p>
                  <p className="text-gray-700">عدد الطلبات: <span className="font-bold">{orders.length}</span></p>
                  <p className="text-gray-700">طلبات السائقين: <span className="font-bold">{drivers.length}</span></p>
                </div>
              </div>
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h3 className="text-xl font-bold mb-4 text-purple-600">إدارة سريعة</h3>
                <p className="text-gray-600">يمكنك إضافة مطاعم ووجبات جديدة وإدارة السائقين من هنا</p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
