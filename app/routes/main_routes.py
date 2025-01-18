from flask import Blueprint, render_template, request
from app.utils.logger import logger
from app.utils.message_utils import create_payload, send_whatsapp_message


bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    logger.info("Index page route is called")
    return render_template('index.html')

@bp.route('/personal', methods=['POST'])
def personal_testing():
    logger.info("Personal Testing route is called")

    template_id = request.form.get('template_id')

    generated_payload = create_payload("personal_testing", template_id, request.form.get('textarea'))
    resp = send_whatsapp_message(generated_payload)

    return resp

@bp.route('/team', methods=['POST'])
def team_testing():
    logger.info("Team Testing route is called")

    template_id = request.form.get('template_id')

    generated_payload = create_payload("team_testing", template_id, request.form.get('textarea'))
    resp = send_whatsapp_message(generated_payload)

    return resp

@bp.route('/authority', methods=['POST'])
def authority_approval():
    logger.info("Authority approval route is called")

    template_id = request.form.get('template_id')

    generated_payload = create_payload("authority_approval", template_id, request.form.get('textarea'))
    resp = send_whatsapp_message(generated_payload)

    return resp

@bp.route('/ap', methods=['POST'])
def ap_list():
    logger.info("AP list route is called")

    template_id = request.form.get('template_id')

    generated_payload = create_payload("ap_list", template_id, request.form.get('textarea'))
    resp = send_whatsapp_message(generated_payload)

    return resp

@bp.route('/employee', methods=['POST'])
def employee_list():
    logger.info("Employee list route is called")

    template_id = request.form.get('template_id')

    generated_payload = create_payload("employee_list", template_id, request.form.get('textarea'))
    resp = send_whatsapp_message(generated_payload)

    return resp
