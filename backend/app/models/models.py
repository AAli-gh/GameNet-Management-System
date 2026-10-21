import enum
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, Enum, Table
)
from sqlalchemy.orm import relationship
from app.database import Base

class UserRole(str, enum.Enum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    OPERATOR = "Operator"

class PCStatusEnum(str, enum.Enum):
    AVAILABLE = "Available"
    IN_USE = "In Use"
    RESERVED = "Reserved"
    OFFLINE = "Offline"
    ERROR = "Error"

class ReservationStatusEnum(str, enum.Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class TariffTypeEnum(str, enum.Enum):
    NORMAL = "Normal"
    VIP = "VIP"
    NIGHT = "Night"
    WEEKEND = "Weekend"

class OrderStatusEnum(str, enum.Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class PaymentMethodEnum(str, enum.Enum):
    CASH = "Cash"
    CARD = "Card"
    WALLET = "Wallet"

pc_games = Table(
    'pc_games',
    Base.metadata,
    Column('pc_id', Integer, ForeignKey('pcs.id', ondelete="CASCADE"), primary_key=True),
    Column('game_id', Integer, ForeignKey('games.id', ondelete="CASCADE"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.OPERATOR, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    audit_logs = relationship("AuditLog", back_populates="user")
    sessions_started = relationship("GameSession", back_populates="operator")

class RolePermission(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(UserRole), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    tariff_type = Column(Enum(TariffTypeEnum), default=TariffTypeEnum.NORMAL)
    hourly_rate = Column(Float, nullable=False)
    half_hourly_rate = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    description = Column(String(255), nullable=True)

    sessions = relationship("GameSession", back_populates="tariff")

class PC(Base):
    __tablename__ = "pcs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    pc_number = Column(Integer, unique=True, nullable=False)
    ip_address = Column(String(45), nullable=True)
    mac_address = Column(String(17), nullable=True)
    is_vip = Column(Boolean, default=False)
    status = Column(Enum(PCStatusEnum), default=PCStatusEnum.OFFLINE)
    current_game = Column(String(100), nullable=True)

    cpu_info = Column(String(100), nullable=True)
    ram_info = Column(String(100), nullable=True)
    gpu_info = Column(String(100), nullable=True)

    status_history = relationship("PCStatus", back_populates="pc", cascade="all, delete-orphan")
    sessions = relationship("GameSession", back_populates="pc")
    reservations = relationship("Reservation", back_populates="pc")
    games = relationship("Game", secondary=pc_games, back_populates="pcs")
    devices = relationship("Device", back_populates="pc")

class PCStatus(Base):
    __tablename__ = "pc_status"

    id = Column(Integer, primary_key=True, index=True)
    pc_id = Column(Integer, ForeignKey("pcs.id", ondelete="CASCADE"), nullable=False)
    cpu_usage = Column(Float, default=0.0)
    ram_usage = Column(Float, default=0.0)
    gpu_usage = Column(Float, default=0.0)
    disk_usage = Column(Float, default=0.0)
    network_status = Column(String(50), default="Connected")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    pc = relationship("PC", back_populates="status_history")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), unique=True, index=True, nullable=False)
    national_id = Column(String(20), nullable=True)
    wallet_balance = Column(Float, default=0.0)
    loyalty_points = Column(Integer, default=0)
    joined_at = Column(DateTime, default=datetime.utcnow)
    last_visit = Column(DateTime, nullable=True)

    sessions = relationship("GameSession", back_populates="customer")
    reservations = relationship("Reservation", back_populates="customer")
    orders = relationship("Order", back_populates="customer")

class GameSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    pc_id = Column(Integer, ForeignKey("pcs.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    tariff_id = Column(Integer, ForeignKey("tariffs.id"), nullable=False)
    operator_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    start_time = Column(DateTime, default=datetime.utcnow, nullable=False)
    end_time = Column(DateTime, nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    remaining_minutes = Column(Integer, nullable=True)

    cost_amount = Column(Float, default=0.0)
    discount_amount = Column(Float, default=0.0)
    final_amount = Column(Float, default=0.0)

    is_active = Column(Boolean, default=True)
    is_paused = Column(Boolean, default=False)
    paused_at = Column(DateTime, nullable=True)
    total_paused_seconds = Column(Integer, default=0)

    notes = Column(Text, nullable=True)

    pc = relationship("PC", back_populates="sessions")
    customer = relationship("Customer", back_populates="sessions")
    tariff = relationship("Tariff", back_populates="sessions")
    operator = relationship("User", back_populates="sessions_started")
    session_logs = relationship("SessionLog", back_populates="session", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="session")

class SessionLog(Base):
    __tablename__ = "session_logs"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id", ondelete="CASCADE"), nullable=False)
    action = Column(String(50), nullable=False)
    details = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    session = relationship("GameSession", back_populates="session_logs")

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    pc_id = Column(Integer, ForeignKey("pcs.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    status = Column(Enum(ReservationStatusEnum), default=ReservationStatusEnum.PENDING)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    pc = relationship("PC", back_populates="reservations")
    customer = relationship("Customer", back_populates="reservations")

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    version = Column(String(50), nullable=True)
    size_gb = Column(Float, default=0.0)
    is_installed = Column(Boolean, default=True)
    icon_url = Column(String(255), nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)

    pcs = relationship("PC", secondary=pc_games, back_populates="games")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)

    order_items = relationship("OrderItem", back_populates="product")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=True)
    total_amount = Column(Float, default=0.0)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.COMPLETED)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="orders")
    session = relationship("GameSession", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    amount = Column(Float, nullable=False)
    method = Column(Enum(PaymentMethodEnum), default=PaymentMethodEnum.CASH)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="payments")

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(String(50), default="INFO")
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String(100), nullable=False)
    details = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="audit_logs")

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    pc_id = Column(Integer, ForeignKey("pcs.id"), nullable=False)
    device_token = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    last_seen = Column(DateTime, default=datetime.utcnow)

    pc = relationship("PC", back_populates="devices")
