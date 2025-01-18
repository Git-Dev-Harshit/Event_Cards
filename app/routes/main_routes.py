from flask import Blueprint, render_template, request
from app.utils.logger import logger
from app.utils.message_utils import create_payload, send_whatsapp_message
from app.utils.image_creation_utils import read_google_sheet, generate_personalized_images

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    logger.info("Index page route is called")
    return render_template('index.html')


@bp.route('/personal', methods=['POST'])
def personal_testing():
    logger.info("Personal Testing route is called")

    data = read_google_sheet("personal_testing")
    image_width = request.form.get('image_width')
    image_height = request.form.get('image_height')
    font_size = request.form.get('font_size')
    starting_point = request.form.get('starting_point')
    card_tag = request.form.get('card_tag')
    regards_color = request.form.get('regards_color')
    name_color = request.form.get('name_color')
    value_color = request.form.get('value_color')
    space_between_lines = request.form.get('space_between_lines')
    template_id = request.form.get('template_id')
    message = request.form.get('textarea')

    logger.info("Generating personalized images for personal testing...")
    generate_personalized_images(data, "personal_testing", image_width, image_height, font_size, starting_point,
                                 card_tag, regards_color, name_color, value_color, space_between_lines)

    logger.info("Generating payload for personal testing...")
    generated_payload = create_payload("personal_testing", template_id, message)

    logger.info("Sending personalized images and text on whatsapp for personal testing team")
    resp = send_whatsapp_message(generated_payload)

    return resp


@bp.route('/team', methods=['POST'])
def team_testing():
    logger.info("Team Testing route is called")


    data = read_google_sheet("team_testing")
    image_width = request.form.get('image_width')
    image_height = request.form.get('image_height')
    font_size = request.form.get('font_size')
    starting_point = request.form.get('starting_point')
    card_tag = request.form.get('card_tag')
    regards_color = request.form.get('regards_color')
    name_color = request.form.get('name_color')
    value_color = request.form.get('value_color')
    space_between_lines = request.form.get('space_between_lines')
    template_id = request.form.get('template_id')
    message = request.form.get('textarea')

    logger.info("Generating personalized images for team_testing...")
    generate_personalized_images(data, "team_testing", image_width, image_height, font_size, starting_point,
                                 card_tag, regards_color, name_color, value_color, space_between_lines)

    logger.info("Generating payload for team_testing...")
    generated_payload = create_payload("team_testing", template_id, message)

    logger.info("Sending personalized images and text on whatsapp for team_testing team")
    resp = send_whatsapp_message(generated_payload)

    return resp


@bp.route('/authority', methods=['POST'])
def authority_approval():
    logger.info("Authority approval route is called")


    data = read_google_sheet("authority_approval")
    image_width = request.form.get('image_width')
    image_height = request.form.get('image_height')
    font_size = request.form.get('font_size')
    starting_point = request.form.get('starting_point')
    card_tag = request.form.get('card_tag')
    regards_color = request.form.get('regards_color')
    name_color = request.form.get('name_color')
    value_color = request.form.get('value_color')
    space_between_lines = request.form.get('space_between_lines')
    template_id = request.form.get('template_id')
    message = request.form.get('textarea')

    logger.info("Generating personalized images for authority_approval...")
    generate_personalized_images(data, "authority_approval", image_width, image_height, font_size, starting_point,
                                 card_tag, regards_color, name_color, value_color, space_between_lines)

    logger.info("Generating payload for authority_approval...")
    generated_payload = create_payload("authority_approval", template_id, message)

    logger.info("Sending personalized images and text on whatsapp for authority_approval team")
    resp = send_whatsapp_message(generated_payload)

    return resp


@bp.route('/ap', methods=['POST'])
def ap_list():
    logger.info("AP list route is called")


    data = read_google_sheet("ap_list")
    image_width = request.form.get('image_width')
    image_height = request.form.get('image_height')
    font_size = request.form.get('font_size')
    starting_point = request.form.get('starting_point')
    card_tag = request.form.get('card_tag')
    regards_color = request.form.get('regards_color')
    name_color = request.form.get('name_color')
    value_color = request.form.get('value_color')
    space_between_lines = request.form.get('space_between_lines')
    template_id = request.form.get('template_id')
    message = request.form.get('textarea')

    logger.info("Generating personalized images for ap_list...")
    generate_personalized_images(data, "ap_list", image_width, image_height, font_size, starting_point,
                                 card_tag, regards_color, name_color, value_color, space_between_lines)

    logger.info("Generating payload for ap_list...")
    generated_payload = create_payload("ap_list", template_id, message)

    logger.info("Sending personalized images and text on whatsapp for ap_list team")
    resp = send_whatsapp_message(generated_payload)

    return resp


@bp.route('/employee', methods=['POST'])
def employee_list():
    logger.info("Employee list route is called")


    data = read_google_sheet("employee_list")
    image_width = request.form.get('image_width')
    image_height = request.form.get('image_height')
    font_size = request.form.get('font_size')
    starting_point = request.form.get('starting_point')
    card_tag = request.form.get('card_tag')
    regards_color = request.form.get('regards_color')
    name_color = request.form.get('name_color')
    value_color = request.form.get('value_color')
    space_between_lines = request.form.get('space_between_lines')
    template_id = request.form.get('template_id')
    message = request.form.get('textarea')

    logger.info("Generating personalized images for employee_list...")
    generate_personalized_images(data, "employee_list", image_width, image_height, font_size, starting_point,
                                 card_tag, regards_color, name_color, value_color, space_between_lines)

    logger.info("Generating payload for employee_list...")
    generated_payload = create_payload("employee_list", template_id, message)

    logger.info("Sending personalized images and text on whatsapp for employee_list team")
    resp = send_whatsapp_message(generated_payload)

    return resp
