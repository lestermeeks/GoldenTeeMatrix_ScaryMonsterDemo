""" Configuration data for the werewolf eyes """
EYE_PATH = __file__[:__file__.rfind('/') + 1]
EYE_DATA = {
    'eye_image'        : EYE_PATH + 'werewolf-eyes.bmp',
    'upper_lid_image'  : EYE_PATH + 'werewolf-upper-lids.bmp',
    'lower_lid_image'  : EYE_PATH + 'werewolf-lower-lids.bmp',
    'stencil_image'    : EYE_PATH + 'werewolf-stencil.bmp',
    'background_image' : EYE_PATH + 'werewolf-background.bmp',
    'transparent'      : (0, 255, 0), # Transparent color in above images
    'eye_move_min'     : (13, -4),    # eye_image (left, top) move limit
    'eye_move_max'     : (23, 5),      # eye_image (right, bottom) move limit
    'upper_lid_open'   : (23, -8),     # upper_lid_image pos when open
    'upper_lid_center' : (23, -3),     # " when eye centered
    'upper_lid_closed' : (23, 8),      # " when closed
    'lower_lid_open'   : (23, 22),     # lower_lid_image pos when open
    'lower_lid_center' : (23, 21),     # " when eye centered
    'lower_lid_closed' : (23, 17),     # " when closed
}
