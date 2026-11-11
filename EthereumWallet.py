import streamlit as st
from web3 import Web3
from eth_account import Account

translations = {
    "Tiếng Việt": {
        "page_title": "Ví Ethereum & Tra cứu Giao dịch",
        "title": "🪙 Ví Ethereum & Tra cứu Giao dịch",
        "caption": "Quản lý ví, chuyển ETH và tra cứu lịch sử giao dịch trực tuyến.",
        "lang_label": "🌍 Chọn ngôn ngữ / Language:",
        "sidebar_net": "⚙️ Cấu hình Mạng",
        "select_net": "Chọn mạng kết nối:",
        "custom_rpc": "Tùy chỉnh (Custom RPC)",
        "connected": "✅ Đã kết nối mạng!",
        "disconnected": "❌ Chưa kết nối. Vui lòng kiểm tra RPC URL.",
        "tabs": ["🆕 Tạo ví mới", "🔍 Kiểm tra số dư", "💸 Gửi ETH", "📜 Tra cứu giao dịch"],
        
        # Tab 1
        "t1_header": "Tạo Ví Ethereum Mới",
        "t1_desc": "Nhấn nút bên dưới để tạo ngẫu nhiên một cặp Địa chỉ ví và Khóa bí mật.",
        "t1_btn": "Tạo ví mới",
        "t1_success": "Tạo ví thành công!",
        "t1_addr": "Địa chỉ ví (Public Address):",
        "t1_pk": "Khóa bí mật (Private Key):",
        "t1_warning": "⚠️ **Cảnh báo bảo mật:** Hãy sao lưu Private Key ở nơi an toàn. Đừng bao giờ chia sẻ khóa này cho bất kỳ ai!",
        
        # Tab 2
        "t2_header": "Kiểm Tra Số Dư",
        "t2_input": "Nhập địa chỉ ví ETH cần kiểm tra:",
        "t2_btn": "Kiểm tra số dư",
        "t2_metric": "Số dư hiện tại",
        "t2_warn": "Vui lòng nhập địa chỉ ví.",
        "t2_err_rpc": "Vui lòng kết nối RPC hợp lệ ở thanh bên trái trước.",
        
        # Tab 3
        "t3_header": "Gửi ETH",
        "t3_pk": "Private Key người gửi:",
        "t3_pk_help": "Private Key để ký giao dịch",
        "t3_recipient": "Địa chỉ người nhận:",
        "t3_amount": "Số lượng ETH muốn gửi:",
        "t3_btn": "Xác nhận & Gửi ETH",
        "t3_spinner": "Đang ký và phát sóng giao dịch lên Blockchain...",
        "t3_success": "Gửi giao dịch thành công!",
        "t3_info": "💡 Mã giao dịch này đã được tự động lưu lại. Bạn có thể sang tab **Tra cứu giao dịch** để kiểm tra ngay.",
        "t3_err_balance": "Số dư ví không đủ trả cả tiền gửi và phí gas!",
        "t3_err_fill": "Vui lòng điền đầy đủ các thông tin giao dịch.",
        
        # Tab 4
        "t4_header": "Tra Cứu Trạng Thái Giao Dịch",
        "t4_desc": "Nhập hoặc sử dụng mã giao dịch (Transaction Hash) vừa thực hiện để tra cứu.",
        "t4_input": "Nhập Tx Hash:",
        "t4_btn": "Tra cứu",
        "t4_spinner": "Đang truy vấn thông tin từ Blockchain...",
        "t4_success_find": "Tìm thấy thông tin giao dịch!",
        "t4_status_succ": "🟢 **Thành công (Success)**",
        "t4_status_fail": "🔴 **Thất bại (Failed)**",
        "t4_from": "Người gửi (From):",
        "t4_to": "Người nhận (To):",
        "t4_value": "Số lượng (ETH):",
        "t4_gas": "Phí Gas tiêu thụ:",
        "t4_block": "Được đưa vào Block số:",
        "t4_err_hash": "Vui lòng nhập mã Tx Hash.",
        "link_detail_mainnet": "🔗 Xem chi tiết trên Mainnet Etherscan"
    },
    "English": {
        "page_title": "Ethereum Wallet & Tracker",
        "title": "🪙 Ethereum Wallet & Tracker",
        "caption": "Manage wallets, send ETH, and track transaction history online.",
        "lang_label": "🌍 Language / Ngôn ngữ:",
        "sidebar_net": "⚙️ Network Configuration",
        "select_net": "Select network:",
        "custom_rpc": "Custom RPC",
        "connected": "✅ Network connected!",
        "disconnected": "❌ Not connected. Please check RPC URL.",
        "tabs": ["🆕 Create Wallet", "🔍 Check Balance", "💸 Send ETH", "📜 Track Transaction"],
        
        # Tab 1
        "t1_header": "Create New Ethereum Wallet",
        "t1_desc": "Click the button below to randomly generate a wallet address and private key.",
        "t1_btn": "Generate New Wallet",
        "t1_success": "Wallet created successfully!",
        "t1_addr": "Public Address:",
        "t1_pk": "Private Key:",
        "t1_warning": "⚠️ **Security Warning:** Back up your Private Key securely. Never share it with anyone!",
        
        # Tab 2
        "t2_header": "Check Balance",
        "t2_input": "Enter ETH wallet address to check:",
        "t2_btn": "Check Balance",
        "t2_metric": "Current Balance",
        "t2_warn": "Please enter a wallet address.",
        "t2_err_rpc": "Please connect a valid RPC in the sidebar first.",
        
        # Tab 3
        "t3_header": "Send ETH",
        "t3_pk": "Sender Private Key:",
        "t3_pk_help": "Private Key to sign the transaction",
        "t3_recipient": "Recipient Address:",
        "t3_amount": "Amount of ETH to send:",
        "t3_btn": "Confirm & Send ETH",
        "t3_spinner": "Signing and broadcasting transaction to Blockchain...",
        "t3_success": "Transaction sent successfully!",
        "t3_info": "💡 This transaction hash has been automatically saved. You can check it in the **Track Transaction** tab.",
        "t3_err_balance": "Insufficient wallet balance to cover both amount and gas fee!",
        "t3_err_fill": "Please fill in all transaction details.",
        
        # Tab 4
        "t4_header": "Track Transaction Status",
        "t4_desc": "Enter or use the recent Transaction Hash to look up details.",
        "t4_input": "Enter Tx Hash:",
        "t4_btn": "Search",
        "t4_spinner": "Querying information from Blockchain...",
        "t4_success_find": "Transaction details found!",
        "t4_status_succ": "🟢 **Success**",
        "t4_status_fail": "🔴 **Failed**",
        "t4_from": "From:",
        "t4_to": "To:",
        "t4_value": "Amount (ETH):",
        "t4_gas": "Gas Used:",
        "t4_block": "Included in Block:",
        "t4_err_hash": "Please enter a Tx Hash.",
        "link_detail_mainnet": "🔗 View details on Mainnet Etherscan"
    }
}

st.set_page_config(
    page_title="Ethereum Wallet",
    page_icon="🪙",
    layout="centered"
)

if "last_tx_hash" not in st.session_state:
    st.session_state.last_tx_hash = ""

st.sidebar.header("🌍 Cài đặt / Settings")
selected_lang = st.sidebar.selectbox("Chọn ngôn ngữ / Language:", ["Tiếng Việt", "English"])
lang = translations[selected_lang]

st.title(lang["title"])
st.caption(lang["caption"])

st.sidebar.header(lang["sidebar_net"])
network_option = st.sidebar.selectbox(
    lang["select_net"],
    ["Ethereum Mainnet", lang["custom_rpc"]]
)

if network_option == "Ethereum Mainnet":
    default_rpc = "https://rpc.ankr.com/eth/bdafa0ec584dca839075d1f265776940e37041c80c43394480fbc7061e04a468"
else:
    default_rpc = ""

rpc_url = st.sidebar.text_input("RPC Provider URL:", value=default_rpc)

# Kiểm tra kết nối Web3
@st.cache_resource(show_spinner=False)
def get_web3_connection(url):
    if not url:
        return None
    w3 = Web3(Web3.HTTPProvider(url))
    return w3 if w3.is_connected() else None

w3 = get_web3_connection(rpc_url)

if w3:
    st.sidebar.success(lang["connected"])
else:
    st.sidebar.error(lang["disconnected"])

tab1, tab2, tab3, tab4 = st.tabs(lang["tabs"])

with tab1:
    st.header(lang["t1_header"])
    st.write(lang["t1_desc"])

    if st.button(lang["t1_btn"], type="primary"):
        new_account = Account.create()
        
        st.success(lang["t1_success"])
        st.text_input(lang["t1_addr"], value=new_account.address, key="new_addr")
        st.text_input(lang["t1_pk"], value=new_account.key.hex(), key="new_pk", type="password")
        
        st.warning(lang["t1_warning"])

with tab2:
    st.header(lang["t2_header"])
    
    check_address = st.text_input(lang["t2_input"], placeholder="0x...")
    
    if st.button(lang["t2_btn"]):
        if not w3:
            st.error(lang["t2_err_rpc"])
        elif not check_address:
            st.warning(lang["t2_warn"])
        else:
            try:
                checksum_address = Web3.to_checksum_address(check_address)
                balance_wei = w3.eth.get_balance(checksum_address)
                balance_eth = w3.from_wei(balance_wei, 'ether')
                
                st.metric(label=lang["t2_metric"], value=f"{balance_eth:.6f} ETH")
            except Exception as e:
                st.error(f"Lỗi / Error: {e}")

with tab3:
    st.header(lang["t3_header"])
    
    with st.form("send_eth_form"):
        sender_pk = st.text_input(lang["t3_pk"], type="password", help=lang["t3_pk_help"])
        recipient_addr = st.text_input(lang["t3_recipient"], placeholder="0x...")
        amount = st.number_input(lang["t3_amount"], min_value=0.0001, step=0.001, format="%.4f")
        
        submit_button = st.form_submit_button(lang["t3_btn"], type="primary")

    if submit_button:
        if not w3:
            st.error(lang["t2_err_rpc"])
        elif not sender_pk or not recipient_addr or amount <= 0:
            st.error(lang["t3_err_fill"])
        else:
            try:
                sender_account = Account.from_key(sender_pk)
                sender_address = sender_account.address
                
                amount_wei = w3.to_wei(amount, 'ether')
                gas_price = w3.eth.gas_price
                estimated_gas = 21000
                total_cost = amount_wei + (estimated_gas * gas_price)
                
                sender_balance = w3.eth.get_balance(sender_address)
                
                if sender_balance < total_cost:
                    st.error(lang["t3_err_balance"])
                else:
                    nonce = w3.eth.get_transaction_count(sender_address)
                    tx = {
                        'nonce': nonce,
                        'to': Web3.to_checksum_address(recipient_addr),
                        'value': amount_wei,
                        'gas': estimated_gas,
                        'gasPrice': gas_price,
                        'chainId': w3.eth.chain_id
                    }
                    
                    with st.spinner(lang["t3_spinner"]):
                        signed_txn = w3.eth.account.sign_transaction(tx, sender_pk)
                        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
                        tx_hash_hex = w3.to_hex(tx_hash)

                    st.session_state.last_tx_hash = tx_hash_hex

                    st.success(lang["t3_success"])
                    st.code(f"Tx Hash: {tx_hash_hex}", language="text")
                    st.info(lang["t3_info"])
                    
                    if network_option == "Ethereum Mainnet":
                        st.markdown(f"[🔗 Xem giao dịch trên Mainnet Etherscan](https://etherscan.io/tx/{tx_hash_hex})")

            except Exception as e:
                st.error(f"Lỗi / Error: {e}")

# --- TAB 4: TRA CỨU GIAO DỊCH ---
with tab4:
    st.header(lang["t4_header"])
    st.write(lang["t4_desc"])
    
    tx_input_hash = st.text_input(
        lang["t4_input"], 
        value=st.session_state.last_tx_hash, 
        placeholder="0x..."
    )
    
    if st.button(lang["t4_btn"]):
        if not w3:
            st.error(lang["t2_err_rpc"])
        elif not tx_input_hash:
            st.warning(lang["t4_err_hash"])
        else:
            try:
                with st.spinner(lang["t4_spinner"]):
                    tx_data = w3.eth.get_transaction(tx_input_hash)
                    tx_receipt = w3.eth.get_transaction_receipt(tx_input_hash)
                
                st.success(lang["t4_success_find"])
                
                status = tx_receipt['status']
                if status == 1:
                    st.markdown(f"### Status: {lang['t4_status_succ']}")
                else:
                    st.markdown(f"### Status: {lang['t4_status_fail']}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.text_input(lang["t4_from"], value=tx_data['from'], disabled=True)
                    st.text_input(lang["t4_to"], value=str(tx_data['to']), disabled=True)
                with col2:
                    value_eth = w3.from_wei(tx_data['value'], 'ether')
                    st.text_input(lang["t4_value"], value=f"{value_eth} ETH", disabled=True)
                    gas_used = tx_receipt['gasUsed']
                    gas_price_gwei = w3.from_wei(tx_data['gasPrice'], 'gwei')
                    st.text_input(lang["t4_gas"], value=f"{gas_used} gas (~{gas_price_gwei} Gwei)", disabled=True)
                
                st.info(f"{lang['t4_block']} **{tx_receipt['blockNumber']}**")
                
                if network_option == "Ethereum Mainnet":
                    st.markdown(f"[{lang['link_detail_mainnet']}](https://etherscan.io/tx/{tx_input_hash})")

            except Exception as e:
                st.error(f"Lỗi / Error: {e}")