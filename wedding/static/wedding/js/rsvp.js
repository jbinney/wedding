$(function() {
  function setUpToggle(name) {
    var inputSelector = 'input[name=' + name + ']';
    var $toggleSection = $('#required_if_' + name);

    $(inputSelector).change(function() {
      toggleHidden($toggleSection, this.value);
    });

    var currentValue = $(inputSelector + ':checked').val()
    toggleHidden($toggleSection, currentValue);
  }

  function toggleHidden($section, value) {
    var shouldHide = value !== 'True';
    $section.toggleClass('hidden', shouldHide);
  }

  setUpToggle('attending');
  setUpToggle('has_significant_other');
});
